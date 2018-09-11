import random

class User:
    userId: int
    username: str
    password: str

    def __init__(self, user_id: int, username: str, password: str):
        self.userId = user_id
        self.username = username
        self.password = password

    def authenticate(self):
        self.userId = random.randint(1, 100)
        return True
