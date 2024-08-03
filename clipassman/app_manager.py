# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import getpass
from clipassman.config import Config
from clipassman.smart_pass_manager import SmartPasswordManager
from clipassman.smart_printer import SmartPrinter


class AppManager:
    
    def __init__(self):
        self._manager = SmartPasswordManager()
        self.__init()

    def __init(self):
        self._manager.load_file()

    @staticmethod
    def _show_logo():
        SmartPrinter.print_center(symbol='*')
        SmartPrinter.print_center(text=Config.name, symbol='*')

    @staticmethod
    def _show_footer():
        SmartPrinter.print_center(text=Config.url, symbol='-')
        SmartPrinter.print_center(text=Config.info, symbol='-')
        SmartPrinter.print_center(symbol='=')

    def _show_error(self, title='ERROR!!!', text='Error! Invalid input.'):
        SmartPrinter.print_center(text=title)
        print(text)
        self._continue()

    def main_menu(self):
        while True:
            SmartPrinter.print_center(text=f'Main Menu | Total passwords: {self._manager.count}', symbol='-')
            print(f'1: Add')
            print(f'2: Get/Del')
            print(f'3: Help')
            print(f'0: Exit')

            cmd = input("Choose an action: ").lower()

            if cmd == '0':
                return
            elif cmd == '1':
                self._add_password()
            elif cmd == '2':
                self._get_password()
            elif cmd == '3':
                self._help()
            else:
                self._show_error()

    def _help(self):
        SmartPrinter.print_center('Help')
        SmartPrinter.print_framed(f'Visit the documentation page: {Config.help_url}')
        SmartPrinter.print_center()
        self._continue()

    def _add_password(self):
        while True:
            SmartPrinter.print_center(text='Add new smart password')
            login = self._get_login()
            secret = self._get_secret(secure_flag=False)
            length = self._get_password_length()
            self._manager.add_smart_password(
                login=login,
                secret=secret,
                length=length
            )
            password = self._manager.generate_smart_password(
                login=login,
                secret=secret,
                length=length,
            )
            self._manager.save_file()
            SmartPrinter.print_center()
            print(f'The new password has been added successfully!')
            SmartPrinter.print_center(text=f'Your smart password:')
            print(password)
            SmartPrinter.print_center()
            self._continue()
            break

    def _get_password(self):
        if not self._manager.count:
            print(f'Smart passwords not found...')
            SmartPrinter.print_center()
            self._continue()
            return
        else:
            while True:
                SmartPrinter.print_center(text='Login list:')
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
                except Exception as s:
                    _ = s
                    self._show_error()
                    continue
                else:
                    login = login_dict[cmd]
                    smart_pass = self._manager.passwords[login]
                    action = self._get_pass_action(smart_pass)
                    if action == 'get':
                        SmartPrinter.print_center(text='Get Smart Password')
                        SmartPrinter.print_framed(f'Login: {smart_pass.login} | Length: {smart_pass.length}')
                        secret = getpass.getpass("Enter secret phrase (hidden): ")
                        check_flag = self._manager.check_public_key(
                            login=smart_pass.login,
                            secret=secret,
                            public_key=smart_pass.key
                        )
                        if check_flag:
                            password = self._manager.generate_smart_password(
                                login=login,
                                secret=secret,
                                length=smart_pass.length
                            )
                            SmartPrinter.print_center(text='Smart Password:')
                            print(password)
                            SmartPrinter.print_center()
                            self._continue()
                        else:
                            self._show_error(text='Error! You have entered incorrect information.')

                    elif action == 'del':
                        self._password_delete(smart_pass.login)
                        SmartPrinter.print_center()
                        print('Password successfully removed!')
                        SmartPrinter.print_center()
                        self._continue()
                        if not self._manager.count:
                            break
                    elif action == 'back':
                        continue

    def _password_delete(self, login):
        self._manager.remove(login)

    def _get_pass_action(self, smart_pass):
        while 1:
            SmartPrinter.print_center()
            SmartPrinter.print_framed(f'Login: {smart_pass.login} | Length: {smart_pass.length}')
            print('1: Get smart password')
            print('2: Delete smart password')
            print('0: <- Back')
            cmd = input('Select the option you want: ')
            if cmd == '1':
                return 'get'
            elif cmd == '2':
                act = input('Are you sure?(y/n): ').lower()
                if act in ['y', 'yes', 'н']:
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
            SmartPrinter.print_framed(f'Attention! Login length must be no less than 4 and no more than 35 characters.')
            login = input('Enter login: ').strip(' ')
            if login in self._manager.passwords.keys():
                print('Error! This login is already in use.')
                login = ''
                self._continue()
                continue
            if len(login) not in range(4, 36):
                print('Error! Invalid login length.')
                login = ''
                self._continue()
                continue
        return login

    def _get_secret(self, secure_flag=True):
        secret = ''
        while not secret:
            if secure_flag:
                secret = getpass.getpass("Enter secret phrase (hidden): ")
            else:
                secret = input('Enter secret phrase: ')
            if not secret:
                print('Error! You did not enter a secret phrase.')
                self._continue()
        return secret

    def _get_password_length(self):
        length = 0
        while not length:
            length = input('Enter password length (10-1000): ')
            try:
                length = abs(int(length))
            except Exception as e:
                _ = e
                length = 0
                print('Error! You did not enter a number.')
                self._continue()
            else:
                length = max(10, min(length, 1000))
        return length

    @staticmethod
    def _continue():
        input('Press enter to continue... ')

    def run(self):
        self._show_logo()
        self.main_menu()
        self._show_footer()
