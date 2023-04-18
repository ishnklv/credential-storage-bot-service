from modules.mongodb import collections
from libs.orm import Orm


user_model: Orm = Orm(collections.get('users'))