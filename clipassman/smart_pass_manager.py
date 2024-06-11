import json
from pathlib import Path

from smartpasslib.generators import SmartPasswordMaster

from clipassman.smart_password_factory import SmartPasswordFactory, SmartPassword


class SmartPasswordManager:
    file_path = Path(Path.home()).joinpath('.cases.json')
    smart_pass_gen = SmartPasswordMaster()
    smart_pass_factory = SmartPasswordFactory()

    def __init__(self):
        self._passwords = {}

    @property
    def passwords(self):
        return self._passwords

    @property
    def count(self):
        return len(self._passwords)

    def add(self, password):
        if password not in self._passwords:
            self._passwords[password.login] = password

    def add_smart_password(self, login, secret, length):
        key = self.smart_pass_gen.get_public_key(login=login, secret=secret)
        smart_password = self.smart_pass_factory.create_smart_password(
            login=login,
            key=key,
            length=length
        )
        self.add(smart_password)
        return smart_password

    def add_passwords(self, passwords):
        for password in passwords:
            if isinstance(password, SmartPassword):
                self.add(password)

    def get_password(self, login):
        return self._passwords.get(login)

    def remove(self, login: str) -> None:
        if login in self._passwords:
            del self._passwords[login]
        self.save_file()

    def load_file(self):
        try:
            with open(self.file_path, 'r') as f:
                json_data = json.load(f)
        except json.decoder.JSONDecodeError:
            return {}
        except FileNotFoundError:
            self.file_path = Path(Path.home()).joinpath('.cases.json')
            self.save_file()
            return {}
        else:
            passwords = [
                SmartPassword(
                    login=json_data[obj]['login'],
                    key=json_data[obj]['key'],
                    length=json_data[obj]['length']
                ) for obj in json_data]
            self.add_passwords(passwords)
            return passwords

    def save_file(self):
        passwords_dict = {name: {'login': password.login,
                                 'length': password.length,
                                 'key': password.key}
                          for name, password in self._passwords.items()}
        self._save_file(passwords_dict)

    def clear(self):
        self._passwords = {}

    def _save_file(self, passwords: dict):
        """Writes json data to a file."""
        with open(self.file_path, 'w') as f:
            json.dump(passwords, f, indent=4)
