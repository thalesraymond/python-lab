class User:
    username: str
    password: str

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def authenticate(self):
        return True
