from src.libs.mongodb import collections
from src.libs.orm import Orm


user_repository: Orm = Orm(collections.get('users'))