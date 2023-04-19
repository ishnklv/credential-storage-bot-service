from modules.mongodb import collections
from libs.orm import Orm

credential_repository: Orm = Orm(collections.get('credentials'))