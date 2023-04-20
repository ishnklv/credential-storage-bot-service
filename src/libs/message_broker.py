import json

from src.settings.config import MESSAGE_BROKER_CONFIG
from redis_client import redis_client

class RedisProducer:
    def __init__(self):
        self.redis = redis_client

    def send_dict(self, data: dict):
        self.redis.publish(MESSAGE_BROKER_CONFIG.get('CHANNEL_NAME'), json.dumps(data))

    def send_str(self, data: str):
        self.redis.publish(MESSAGE_BROKER_CONFIG.get('CHANNEL_NAME'), data)


class RedisConsumer:
    def __init__(self):
        self.redis = redis_client
        self.publication = redis_client.pubsub()
        self.publication.subscribe(MESSAGE_BROKER_CONFIG.get('CHANNEL_NAME'))

    def listen(self):
        return self.publication.listen()
