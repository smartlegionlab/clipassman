# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import click

from smartcliapp import CliManager

from smartpasslib.generators import SmartPasswordMaster

from clipassman.passman import SmartPassMan, SmartPassword


class Commander:
    def __init__(self):
        self._cli_man = CliManager()
        self._pass_man = SmartPassMan()
        self._generator = SmartPasswordMaster()

    def run(self):
        self._load()

        while 1:
            self._cli_man.printer.smart.echo(f'Main menu', '=')
            self._cli_man.printer.smart.echo(f'Passwords: [{self._pass_man.count}]', '-')
            self._cli_man.printer.base.echo('n: new password')
            self._cli_man.printer.base.echo('g: get password')
            self._cli_man.printer.base.echo('r: remove password')
            self._cli_man.printer.base.echo('q: quit')
            self._cli_man.printer.smart.echo()

            char = click.getchar()

            if char.lower() in ('q', 'й'):
                self.quit()
                break
            elif char.lower() in ('n', 'т'):
                self.new()
            elif char.lower() in ('g', 'п'):
                self.get()
            elif char.lower() in ('r', 'к'):
                self.remove()
            else:
                self._cli_man.printer.base.echo('Invalid input!')

    def new(self):
        self._cli_man.printer.smart.echo('Create new password', '=')
        login = self._get_login()
        secret = self._get_secret()
        length = self._get_length()
        key = self._generator.get_public_key(login=login, secret=secret)
        smart_password = SmartPassword(login=login, key=key, length=length)
        password = self._generator.get_smart_password(login=login, secret=secret, length=length)
        self._show_password(password=password)
        self._to_continue()
        self._pass_man.add(smart_password)

    def get(self):
        self._cli_man.printer.smart.echo('Get password', '=')
        if self._pass_man.passwords:
            while 1:
                smart_password = self._get_smart_password()

                if smart_password is not None:
                    self._cli_man.printer.smart.echo(f'Password for: {smart_password.login}')
                    self._cli_man.printer.base.echo(f'To generate a password, you will need the secret phrase '
                                                    f'that you used when creating it.')
                    secret = self._get_secret()
                    status = self._generator.check_data(
                        login=smart_password.login,
                        secret=secret,
                        public_key=smart_password.key,
                    )

                    if status:
                        password = self._generator.get_smart_password(
                            login=smart_password.login,
                            secret=secret,
                            length=smart_password.length,
                        )
                        self._show_password(password=password)
                        self._to_continue()
                        break
                    else:
                        self._cli_man.printer.base.echo('Error! You entered incorrect data!')
                        self._to_continue()
                        continue
                else:
                    break
        else:
            self._err_not_found()

    def remove(self):
        self._cli_man.printer.smart.echo('Remove password', '=')
        if self._pass_man.passwords:
            while 1:
                smart_password = self._get_smart_password()

                if smart_password is not None:
                    self._cli_man.printer.smart.echo()
                    action = self._cli_man.get_action(
                        f'Attention! Do you really want to delete: [{smart_password.login}]?')

                    if action:
                        self._pass_man.remove(smart_password.login)
                        self._cli_man.printer.base.echo('Login deleted successfully!')
                        self._pass_man.save_file()
                        self._to_continue()
                        if self._pass_man.passwords:
                            continue
                    else:
                        self._cli_man.printer.base.echo('Login not deleted!')
                        self._to_continue()
                        continue
                break
        else:
            self._err_not_found()

    def _load(self):
        self._pass_man.load_file()

    def quit(self):
        self._save()

    def _save(self):
        self._pass_man.save_file()

    @classmethod
    def _get_login(cls) -> str:
        login = click.prompt(f'Enter a name or login', type=click.STRING)
        return login

    @classmethod
    def _get_secret(cls) -> str:
        secret = click.prompt(f'Enter your secret phrase', type=click.STRING, hide_input=True)
        return secret

    @classmethod
    def _get_length(cls, start: int = 4, end: int = 1000):
        length = click.prompt(
            f'Password length ({start}-{end})',
            type=click.IntRange(start, end, clamp=True)
        )
        return length

    def _show_password(self, password):
        self._cli_man.printer.smart.echo('Your password: ')
        self._cli_man.printer.base.echo()
        self._cli_man.printer.base.echo(password)
        self._cli_man.printer.base.echo()
        self._cli_man.printer.smart.echo()

    @classmethod
    def _to_continue(cls):
        input('Enter to continue...')

    def _get_smart_password(self):
        num_logins = {str(n): password for n, password in enumerate(self._pass_man.passwords, 1)}
        while 1:
            self._cli_man.printer.smart.echo()
            self._cli_man.printer.base.echo('Select the desired login, enter its number and click ENTER (b - Back): ')
            self._cli_man.printer.smart.echo()
            for n, l in num_logins.items():
                print(f'{n}: {l}')

            self._cli_man.printer.smart.echo()
            char = self._cli_man.input('Enter: ')

            if char == 'b':
                return None

            if char in num_logins:
                login = num_logins[char]
                smart_password = self._pass_man.passwords[login]
                return smart_password
            else:
                self._cli_man.printer.base.echo('Input error!')
                self._to_continue()

    def _err_not_found(self):
        self._cli_man.printer.base.echo('Logins not found!')
        self._to_continue()
