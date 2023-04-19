from redis import Redis


from settings.config import REDIS_CONFIG

redis_client = Redis(
    host=REDIS_CONFIG.get('host'),
    port=REDIS_CONFIG.get('port'),
    decode_responses=REDIS_CONFIG.get('decode_response'),
    db=REDIS_CONFIG.get('db')
)