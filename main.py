import datetime
import tracemalloc
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

from utils import generate_password, is_valid_login
from settings.config import BOT_CONFIG
from repositories.credential_repository import credential_repository
from entities.credential_entity import Credential

tracemalloc.start()

bot = Bot(BOT_CONFIG.get('API_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class CreateCredentialForm(StatesGroup):
    waiting_for_service_name = State()
    waiting_for_login = State()
    waiting_for_password_type = State()
    waiting_for_password = State()


class GetCredentialForm(StatesGroup):
    waiting_for_service_name = State()


class SecurityStates(StatesGroup):
    waiting_for_password = State()


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    # создаем клавиатуру с кнопкой /create_credential
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('/create_credential')
    button2 = KeyboardButton('/get_credential')
    button3 = KeyboardButton('/list_credentials')
    button4 = KeyboardButton('/help')
    keyboard.add(button1, button2, button3, button4)

    # отправляем сообщение пользователю
    await message.answer("Hello! What do you want to do?", reply_markup=keyboard)


@dp.message_handler(Command("help"))
async def cmd_start(message: types.Message):
    # создаем клавиатуру с кнопкой /create_credential
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('/create_credential')
    button2 = KeyboardButton('/get_credential')
    button3 = KeyboardButton('/list_credentials')
    button4 = KeyboardButton('/help')
    keyboard.add(button1, button2, button3, button4)

    # отправляем сообщение пользователю
    await message.answer("Commands List:", reply_markup=keyboard)


@dp.message_handler(Command("create_credential"))
async def create_credential(message: types.Message):
    await CreateCredentialForm.waiting_for_service_name.set()
    await message.answer("Enter service name:")


@dp.message_handler(Command("get_credential"))
async def get_credential(message: types.Message):
    await GetCredentialForm.waiting_for_service_name.set()
    await message.answer("Enter service name:")


@dp.message_handler(Command("list_credentials"))
async def list_credentials(message: types.Message):
    user_id = message.from_user.id

    query = {
        'telegram_user_id': user_id,
    }

    items = credential_repository.find(query)

    message_text = ""
    for dictionary in items:
        if "created_at" in dictionary:
            created_date = datetime.strptime(dictionary["created_at"], "%Y-%m-%d")
            message_text += f"Service name: {dictionary['service_name']}\nLogin: {dictionary['login']}\nPassword: {dictionary['password']}\nCreated Date: {created_date.strftime('%d.%m.%Y')}\n\n"
        else:
            message_text += f"Service name: {dictionary['service_name']}\nLogin: {dictionary['login']}\nPassword: {dictionary['password']}\nCreated Date: {datetime.datetime.now().strftime('%d.%m.%Y')}\n\n"

    await message.answer(message_text)

    count = credential_repository.count(query)

    await message.answer(f"Counts: {count}")


@dp.message_handler(state=GetCredentialForm.waiting_for_service_name)
async def process_get_credential_by_service_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_name'] = message.text

    credential = credential_repository.find_one(
        {'telegram_user_id': message.from_user.id, 'service_name': data.get('service_name')})

    if not credential:
        await message.answer("Credential by service name not found")
        return

    await state.finish()
    await message.answer(
        f"Service name: {credential['service_name']}\nLogin: {credential['login']}\nPassword: {credential['password']}")


@dp.message_handler(state=CreateCredentialForm.waiting_for_service_name)
async def process_service_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_name'] = message.text

    await CreateCredentialForm.waiting_for_login.set()
    await message.answer("Enter service login:")


@dp.message_handler(state=CreateCredentialForm.waiting_for_login)
async def process_login(message: types.Message, state: FSMContext):
    if not is_valid_login(message.text):
        await message.answer("Login invalid, please retype login")
        return

    async with state.proxy() as data:
        data['login'] = message.text

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Generate"), KeyboardButton("Enter"))
    await CreateCredentialForm.waiting_for_password_type.set()
    await message.answer("Generate or enter password:", reply_markup=keyboard)


@dp.message_handler(Text(equals="Generate"), state=CreateCredentialForm.waiting_for_password_type)
async def process_password_generate(message: types.Message, state: FSMContext):
    password = generate_password()

    async with state.proxy() as data:
        data['password'] = password
        data['password_is_generated'] = True

    credential = save_credential(data=data, user_id=message.from_user.id)

    await state.finish()

    await message.answer(credential.display())


@dp.message_handler(Text(equals="Enter"), state=CreateCredentialForm.waiting_for_password_type)
async def process_password_enter(message: types.Message):
    await CreateCredentialForm.waiting_for_password.set()
    await message.answer("Enter password:")


@dp.message_handler(state=CreateCredentialForm.waiting_for_password)
async def process_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        data['password_is_generated'] = False

    credential = save_credential(data=data, user_id=message.from_user.id)

    await state.finish()

    await message.answer(credential.display())


def save_credential(data, user_id):
    credential = Credential({
        'service_name': data['service_name'],
        'login': data['login'],
        'password': data['password'],
        'telegram_user_id': user_id,
    })

    credential_repository.create(credential.to_document())

    return credential


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
