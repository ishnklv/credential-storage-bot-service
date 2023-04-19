import datetime
import json
import uuid


class Credential:
    service_name: str
    login: str
    password: str
    password_is_generated: bool
    telegram_user_id: int

    is_deleted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, props):
        self.id = uuid.uuid4()
        self.service_name = props.get('service_name')
        self.login = props.get('login')
        self.password = props.get('password')
        self.password_is_generated = props.get('password_is_generated')
        self.telegram_user_id = props.get('telegram_user_id')

        self.is_deleted = False
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def to_domain(self):
        return {
            'id': self.id,
            'props': {
                'service_name': self.service_name,
                'login': self.login,
                'password': self.password,
                'password_is_generated': self.password_is_generated,
            },
            'params': {
                'is_deleted': self.is_deleted,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
            },
            'author': {
                'id': self.telegram_user_id,
            }
        },

    def to_document(self):
        return {
            'domain_id': str(self.id),
            'service_name': self.service_name,
            'login': self.password,
            'password': self.password,
            'password_is_generated': self.password_is_generated,
            'is_deleted': self.is_deleted,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def to_json(self):
        return json.dumps({
            'service_name': self.service_name,
            'login': self.login,
            'password': self.password,
            'password_is_generated': self.password_is_generated,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'telegram_user_id': self.telegram_user_id,
        })

    def display(self):
        return f"Service_name: {self.service_name}\nLogin: {self.login}\nPassword: {self.password}\nCreated At: {self.created_at.strftime('%d.%m.%Y')}"
