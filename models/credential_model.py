from modules.mongodb import collections
from libs.orm import Orm


credential_model: Orm = Orm(collections.get('credentials'))