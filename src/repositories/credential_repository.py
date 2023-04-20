from src.storages.mongodb import collections
from src.libs.orm import Orm

credential_repository: Orm = Orm(collections.get('credentials'))