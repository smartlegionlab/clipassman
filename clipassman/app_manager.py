import getpass
from clipassman.config import Config
from clipassman.output_manager import OutputManager
from clipassman.smart_pass_manager import SmartPasswordManager


class AppManager:
    
    def __init__(self):
        self.printer = OutputManager()
        self.manager = SmartPasswordManager()
        self.config = Config()
        self._init()

    def _init(self):
        self.manager.load_file()

    def show_logo(self):
        self.printer.print_text(symbol='*')
        self.printer.print_text(text=self.config.name, symbol='*')

    def show_footer(self):
        self.printer.print_text(text=self.config.url, symbol='-')
        self.printer.print_text(text=self.config.info, symbol='-')
        self.printer.print_text(symbol='=')

    def main_menu(self):
        while True:
            self.printer.print_text(text=f'Total passwords: {self.manager.count}', symbol='-')
            print(f'a: Add password')
            print(f'g: Get password')
            print(f'h: Help')
            print(f'e: Exit')

            self.printer.print_text()
            cmd = input("Choose an action: ")
            self.printer.print_text()

            if cmd == 'e':
                return
            elif cmd == 'a':
                self.add_password()
            elif cmd == 'g':
                self.get_password()
            elif cmd == 'h':
                print(f'Visit the documentation page: {self.config.url}')
                input('Enter to continue...')
            else:
                print('Wrong option...')
            self.printer.print_text()

    def add_password(self):
        while True:
            login = self.get_login()
            secret = self.get_secret()
            length = self.get_password_length()
            self.manager.add_smart_password(
                login=login,
                secret=secret,
                length=length
            )
            password = self.manager.smart_pass_gen.get_smart_password(
                login=login,
                secret=secret,
                length=length,
            )
            self.manager.save_file()
            print(f'The new password has been added successfully.')
            self.printer.print_text()
            print(f'Your smart password:')
            print(password)
            self.printer.print_text()
            input('Enter to continue...')
            break

    def get_password(self):
        if not self.manager.count:
            print(f'Not found...')
            return
        else:
            while True:
                self.printer.print_text(text='Login list:')
                login_dict = {
                    n: login for n, login in enumerate(self.manager.passwords.keys(), 1)
                }
                for key, val in login_dict.items():
                    print(f'{key}. {val}')
                print('0. Back')
                cmd = input('Select the option you want: ')
                if cmd == '0':
                    return

    def get_login(self):
        login = ''
        while not login:
            login = input('Enter login: ')
            if login in self.manager.passwords.keys():
                print('Error! This login is already in use.')
                login = ''
                continue
            if not login:
                print('Error! You have not entered your login.')
        return login

    @staticmethod
    def get_secret():
        secret = ''
        while not secret:
            secret = getpass.getpass("Enter secret phrase (hidden): ")
            if not secret:
                print('Error! You did not enter a secret phrase.')
        return secret

    @staticmethod
    def get_password_length():
        length = 0
        while not length:
            length = input('Enter password length (4-1000): ')
            try:
                length = abs(int(length))
                if length < 4 or length > 1000:
                    if length < 4:
                        length = 4
                    if length > 1000:
                        length = 1000
            except Exception:
                print('Error! You did not enter a number.')
                length = 0
        return length

    def run(self):
        self.show_logo()
        self.main_menu()
        self.show_footer()
