import json
import shutil
from pathlib import Path

from smartpasslib.generators import SmartPasswordMaster

from clipassman.config import Config


class OutputManager:

    @classmethod
    def print_text(self, text='', symbol='-'):
        width = self._get_term_width()
        text = f' {text} ' if text else ''
        print(text.center(width, symbol))

    @classmethod
    def _get_term_width(self):
        return shutil.get_terminal_size()[0]


class SmartPassword:

    def __init__(self, login='', key='', length=12):
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        """Get login"""
        return self._login

    @property
    def key(self):
        """get public key"""
        return self._key

    @property
    def length(self):
        """Get password length"""
        return self._length


class SmartPassMan:
    file = Path(Path.home()).joinpath('.cases.json')

    def __init__(self):
        self._generators = SmartPasswordMaster()
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

    def add_smart_pass(self, login, secret, length):
        key = self._generators.get_public_key(login=login, secret=secret)
        smart_password = SmartPassword(login=login, key=key, length=length)
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

    def load_file(self):
        try:
            with open(self.file, 'r') as f:
                json_data = json.load(f)
        except json.decoder.JSONDecodeError:
            return {}
        except FileNotFoundError:
            self.file = Path(Path.home()).joinpath('.cases.json')
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
        with open(self.file, 'w') as f:
            json.dump(passwords, f, indent=4)


class AppManager:
    
    def __init__(self):
        self.printer = OutputManager()
        self.manager = SmartPassMan()
        self.config = Config()
        self._init()

    def _init(self):
        self.manager.load_file()

    def show_logo(self):
        self.printer.print_text(symbol='*')
        self.printer.print_text(text=self.config.name, symbol='*')
        self.printer.print_text(text=f'Total passwords: {self.manager.count}', symbol='-')

    def show_footer(self):
        self.printer.print_text(text=self.config.url, symbol='-')
        self.printer.print_text(text=self.config.info, symbol='-')
        self.printer.print_text(symbol='=')

    def main_menu(self):
        while True:
            print(f'a: Add password')
            print(f'g: Get password')
            print(f'e: Exit')

            self.printer.print_text()
            choice = input("Choose an action: ")
            self.printer.print_text()

            if choice == 'e':
                return
            elif choice == 'a':
                self.add_password()
            elif choice == 'g':
                self.get_password()
            else:
                print('Wrong option...')
            self.printer.print_text()

    def add_password(self):
        print('Show add password menu')

    def get_password(self):
        print('Show get password menu')

    def run(self):
        self.show_logo()
        self.main_menu()
        self.show_footer()
