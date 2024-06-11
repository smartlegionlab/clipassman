import getpass
from clipassman.config import Config
from clipassman.output_manager import OutputManager
from clipassman.smart_pass_manager import SmartPasswordManager


class AppManager:
    
    def __init__(self):
        self._printer = OutputManager()
        self._manager = SmartPasswordManager()
        self._config = Config()
        self.__init()

    def __init(self):
        self._manager.load_file()

    def _show_logo(self):
        self._printer.print_text(symbol='*')
        self._printer.print_text(text=self._config.name, symbol='*')

    def _show_footer(self):
        self._printer.print_text(text=self._config.url, symbol='-')
        self._printer.print_text(text=self._config.info, symbol='-')
        self._printer.print_text(symbol='=')

    def _show_error(self, title='ERROR!!!', text='Error! Invalid input.'):
        self._printer.print_text(text=title)
        print(text)
        input('Enter to continue...')

    def main_menu(self):
        while True:
            self._printer.print_text(text=f'Main Menu | Total passwords: {self._manager.count}', symbol='-')
            print(f'a: Add')
            print(f'g: Get/Del')
            print(f'h: Help')
            print(f'e: Exit')

            cmd = input("Choose an action: ")

            if cmd == 'e':
                return
            elif cmd == 'a':
                self._add_password()
            elif cmd == 'g':
                self._get_password()
            elif cmd == 'h':
                self._help()
            else:
                self._show_error()

    def _help(self):
        self._printer.print_text('Help')
        print(f'Visit the documentation page: {self._config.url}')
        self._printer.print_text()
        input('Enter to continue...')

    def _add_password(self):
        while True:
            self._printer.print_text(text='Add new smart password')
            login = self._get_login()
            secret = self._get_secret()
            length = self._get_password_length()
            self._manager.add_smart_password(
                login=login,
                secret=secret,
                length=length
            )
            password = self._manager.smart_pass_gen.get_smart_password(
                login=login,
                secret=secret,
                length=length,
            )
            self._manager.save_file()
            print(f'The new password has been added successfully.')
            self._printer.print_text(text=f'Your smart password:')
            print(password)
            self._printer.print_text()
            input('Enter to continue...')
            break

    def _get_password(self):
        if not self._manager.count:
            print(f'Smart passwords not found...')
            self._printer.print_text()
            input('Enter to continue...')
            return
        else:
            while True:
                self._printer.print_text(text='Login list:')
                login_dict = {
                    n: login for n, login in enumerate(self._manager.passwords.keys(), 1)
                }
                for key, val in login_dict.items():
                    print(f'{key}. {val}')
                print('0. <- Back')
                cmd = input('Select: ')
                try:
                    cmd = abs(int(cmd))
                    if not cmd:
                        return
                    if cmd not in login_dict:
                        raise ValueError
                except:
                    self._show_error()
                    continue
                else:
                    login = login_dict[cmd]
                    smart_pass = self._manager.passwords[login]
                    action = self._get_pass_action(smart_pass)
                    if action == 'get':
                        self._printer.print_text(text='Get Smart Password')
                        print(f'Login: {smart_pass.login} | Length: {smart_pass.length}')
                        secret = getpass.getpass("Enter secret phrase (hidden): ")
                        check_flag = self._manager.smart_pass_gen.check_data(
                            login=smart_pass.login,
                            secret=secret,
                            public_key=smart_pass.key
                        )
                        if check_flag:
                            password = self._manager.smart_pass_gen.get_smart_password(
                                login=login,
                                secret=secret,
                                length=smart_pass.length
                            )
                            self._printer.print_text(text='Smart Password:')
                            print(password)
                            self._printer.print_text()
                            input('Enter to continue...')
                        else:
                            self._show_error(text='Error! You have entered incorrect information.')

                    elif action == 'del':
                        self._password_delete(smart_pass.login)
                        self._printer.print_text()
                        print('Password successfully removed!')
                        self._printer.print_text()
                        input('Enter to continue...')
                        if not self._manager.count:
                            break
                    elif action == 'back':
                        continue

    def _password_delete(self, login):
        self._manager.remove(login)

    def _get_pass_action(self, smart_pass):
        while 1:
            self._printer.print_text(text=f'Login: {smart_pass.login} | Length: {smart_pass.length}')
            print('1: Get smart password')
            print('2: Delete smart password')
            print('0: <- Back')
            cmd = input('Select the option you want: ')
            if cmd == '1':
                return 'get'
            elif cmd == '2':
                act = input('Are you sure?(y/n): ')
                if act in ['y', '']:
                    return 'del'
                else:
                    continue
            elif cmd == '0':
                return 'back'
            else:
                self._show_error()

    def _get_login(self):
        login = ''
        while not login:
            login = input('Enter login: ')
            if login in self._manager.passwords.keys():
                print('Error! This login is already in use.')
                login = ''
                continue
            if not login:
                print('Error! You have not entered your login.')
        return login

    @staticmethod
    def _get_secret():
        secret = ''
        while not secret:
            secret = getpass.getpass("Enter secret phrase (hidden): ")
            if not secret:
                print('Error! You did not enter a secret phrase.')
        return secret

    @staticmethod
    def _get_password_length():
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
        self._show_logo()
        self.main_menu()
        self._show_footer()
