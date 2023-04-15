from pymongo import MongoClient, errors
from config import MONGODB_CONFIG
from logger import logger

try:
    mongodb_client = MongoClient(host=MONGODB_CONFIG.get('host'), port=MONGODB_CONFIG.get('port'))
    logger.info('Connection to mongodb successfully')
except errors.ConnectionFailure as err:
    logger.error('Connection to mongodb failed', err)
    raise ValueError('Connection to mongodb failed', err)

database = mongodb_client[MONGODB_CONFIG.get('database')]

collections = {
    'users': database['users'],
    'credentials': database['credentials']
}
