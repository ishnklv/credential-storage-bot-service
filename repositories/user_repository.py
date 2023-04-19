from modules.mongodb import collections
from libs.orm import Orm


user_repository: Orm = Orm(collections.get('users'))