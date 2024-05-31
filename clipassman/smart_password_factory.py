

class SmartPassword:

    def __init__(self, login='', key='', length=12):
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        return self._login

    @property
    def key(self):
        return self._key

    @property
    def length(self):
        return self._length


class SmartPasswordFactory:

    @classmethod
    def create_smart_password(cls, login, key, length):
        return SmartPassword(login=login, key=key, length=length)
