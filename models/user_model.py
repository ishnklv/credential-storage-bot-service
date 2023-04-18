from modules.mongodb import collections
from libs.orm import Orm


user_model = Orm(collections.get('users'))