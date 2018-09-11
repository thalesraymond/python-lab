from typing import List

from domain.user import User
from infrastructure.repository import engineFactory


class UserRepository:

    def __init__(self):
        self.engine = engineFactory.engine

    def get_user(self) -> List[User]:
        return None
        # No user table yet
