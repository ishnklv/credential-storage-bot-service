import os
from dotenv import load_dotenv

load_dotenv()

BOT_CONFIG = {
    'API_TOKEN': os.getenv('BOT_API_TOKEN'),
}

MESSAGE_BROKER_CONFIG = {
    'CHANNEL_NAME': os.getenv('MESSAGE_BROKER_CHANNEL_NAME'),
}

REDIS_CONFIG = {
    'host': os.getenv('REDIS_HOST'),
    'port': int(os.getenv('REDIS_PORT')),
    'decode_response': True,
    'db': 0
}

MONGODB_CONFIG = {
    'host': os.getenv('MONGODB_HOST'),
    'port': int(os.getenv('MONGODB_PORT')),
    'database': os.getenv('MONGODB_DATABASE'),
}