import json
from redis import Redis

from settings.config import REDIS_CONFIG, MESSAGE_BROKER_CONFIG

redis_client = Redis(
    host=REDIS_CONFIG.get('host'),
    port=REDIS_CONFIG.get('port'),
    decode_responses=REDIS_CONFIG.get('decode_response'),
    db=REDIS_CONFIG.get('db')
)


class Producer:
    def __init__(self):
        self.redis = redis_client

    def send_dict(self, data: dict):
        self.redis.publish(MESSAGE_BROKER_CONFIG.get('CHANNEL_NAME'), json.dumps(data))

    def send_str(self, data: str):
        self.redis.publish(MESSAGE_BROKER_CONFIG.get('CHANNEL_NAME'), data)