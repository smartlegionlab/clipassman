# Copyright © 2025, Alexander Suvorov
import getpass
from clipassman.config import Config
from clipassman.smart_printer import SmartPrinter
from smartpasslib import SmartPasswordManager, SmartPasswordMaster


class AppManager:

    def __init__(self):
        self._manager = SmartPasswordManager()

    @staticmethod
    def _show_logo():
        SmartPrinter.print_center(symbol='*')
        SmartPrinter.print_center(text=Config.name, symbol='*')
        SmartPrinter.print_center(text=f"Version: v2.0.0", symbol='*')

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
            SmartPrinter.print_center(text=f'Main Menu | Total passwords: {self._manager.password_count}', symbol='-')
            print(f'1: Add Password')
            print(f'2: Get/Delete Password')
            print(f'3: Clear All Passwords')
            print(f'4: Help')
            print(f'0: Exit')

            cmd = input("Choose an action: ").lower()

            if cmd == '0':
                return
            elif cmd == '1':
                self._add_password()
            elif cmd == '2':
                self._get_password()
            elif cmd == '3':
                self._clear_passwords()
            elif cmd == '4':
                self._help()
            else:
                self._show_error()

    def _help(self):
        SmartPrinter.print_center('Help')
        print("""
        SMART PASSWORD MANAGER v2.0.0
        =============================

        Breaking Changes from v1.x:
        • Login parameter removed - now uses only secret phrase
        • All v1.x passwords are INVALID
        • You must create NEW passwords

        How it works:
        1. You provide a description and secret phrase
        2. System generates a public key from the secret
        3. Password is generated deterministically
        4. Only description and public key are stored

        To retrieve a password:
        1. Select password entry
        2. Enter the same secret phrase
        3. Password is regenerated

        Security Notes:
        • Passwords are never stored
        • Same secret → same password every time
        • Case-sensitive secret phrases
        """)
        SmartPrinter.print_framed(f'Documentation: {Config.help_url}')
        SmartPrinter.print_center()
        self._continue()

    def _add_password(self):
        while True:
            SmartPrinter.print_center(text='Add new smart password')
            description = self._get_description()
            secret = self._get_secret(secure_flag=False)
            length = self._get_password_length()

            try:
                public_key = SmartPasswordMaster.generate_public_key(secret=secret)

                if public_key in self._manager.passwords:
                    existing = self._manager.passwords[public_key]
                    SmartPrinter.print_center(text="WARNING!")
                    print(f"A password with this secret phrase already exists:")
                    print(f"Description: {existing.description}")
                    print(f"Length: {existing.length} characters")
                    print("\nEach unique secret phrase can have only one entry.")
                    self._continue()
                    continue

                from smartpasslib import SmartPassword
                smart_password = SmartPassword(
                    public_key=public_key,
                    description=description,
                    length=length
                )

                self._manager.add_smart_password(smart_password)

                password = SmartPasswordMaster.generate_smart_password(
                    secret=secret,
                    length=length
                )

                SmartPrinter.print_center()
                print(f'✓ Password metadata added successfully!')
                print(f'Description: {description}')
                print(f'Length: {length} characters')
                print(f'Public Key: {public_key[:16]}...{public_key[-16:]}')
                SmartPrinter.print_center(text='Your generated password:')
                print(password)
                SmartPrinter.print_center()

            except Exception as e:
                self._show_error(text=f'Failed to create password: {str(e)}')
                continue

            self._continue()
            break

    def _get_password(self):
        if not self._manager.password_count:
            print(f'No password entries found...')
            SmartPrinter.print_center()
            self._continue()
            return

        while True:
            SmartPrinter.print_center(text='Password List:')
            password_list = list(self._manager.passwords.values())

            for idx, smart_pass in enumerate(password_list, 1):
                print(f'{idx}. {smart_pass.description} ({smart_pass.length} chars)')

            print('0. ← Back')
            cmd = input('Select entry: ')

            try:
                cmd = abs(int(cmd))
                if cmd == 0:
                    return
                if cmd > len(password_list):
                    raise ValueError
            except ValueError:
                self._show_error()
                continue

            selected_pass = password_list[cmd - 1]
            action = self._get_pass_action(selected_pass)

            if action == 'get':
                self._retrieve_password(selected_pass)
            elif action == 'del':
                self._delete_password(selected_pass)
                if not self._manager.password_count:
                    break
            elif action == 'back':
                continue

    def _retrieve_password(self, smart_pass):
        SmartPrinter.print_center(text='Retrieve Smart Password')
        print(f'Description: {smart_pass.description}')
        print(f'Length: {smart_pass.length} characters')

        secret = getpass.getpass("Enter secret phrase (hidden): ")

        try:
            is_valid = SmartPasswordMaster.check_public_key(
                secret=secret,
                public_key=smart_pass.public_key
            )

            if is_valid:
                password = SmartPasswordMaster.generate_smart_password(
                    secret=secret,
                    length=smart_pass.length
                )

                SmartPrinter.print_center(text='Generated Password:')
                print(password)
                SmartPrinter.print_center()
            else:
                self._show_error(
                    title='Invalid Secret',
                    text='The secret phrase is incorrect.\n'
                         'Check: Caps Lock, keyboard layout, spelling.\n'
                         'Note: Secret phrases are case-sensitive.'
                )

        except Exception as e:
            self._show_error(text=f'Failed to generate password: {str(e)}')

        self._continue()

    def _delete_password(self, smart_pass):
        confirm = input(f"Delete '{smart_pass.description}'? (y/n): ").lower()
        if confirm in ['y', 'yes']:
            try:
                self._manager.delete_smart_password(smart_pass.public_key)
                print(f"✓ '{smart_pass.description}' deleted successfully!")
            except KeyError:
                print(f"Error: Password entry not found")
        else:
            print("Deletion cancelled")

    def _clear_passwords(self):
        if self._manager.password_count == 0:
            print("No passwords to clear")
            self._continue()
            return

        confirm = input(f"Clear ALL {self._manager.password_count} password entries? (y/n): ").lower()
        if confirm in ['y', 'yes']:
            confirm2 = input("This cannot be undone. Type 'DELETE ALL' to confirm: ")
            if confirm2 == 'DELETE ALL':
                self._manager.clear()
                print(f"✓ All {self._manager.password_count} password entries cleared!")
            else:
                print("Clear operation cancelled")
        else:
            print("Clear operation cancelled")

        self._continue()

    def _get_pass_action(self, smart_pass):
        while True:
            SmartPrinter.print_center()
            print(f'Selected: {smart_pass.description}')
            print(f'Length: {smart_pass.length} characters')
            print('1: Get password')
            print('2: Delete entry')
            print('0: ← Back')
            cmd = input('Select action: ')

            if cmd == '1':
                return 'get'
            elif cmd == '2':
                return 'del'
            elif cmd == '0':
                return 'back'
            else:
                self._show_error()

    def _get_description(self):
        description = ''
        while not description:
            SmartPrinter.print_framed(
                'Enter a descriptive name for this password (e.g., "GitHub Account", "Bank Login")')
            description = input('Description: ').strip()

            if not description:
                print('Error: Description cannot be empty')
                self._continue()
                continue

            if len(description) > 100:
                print('Error: Description too long (max 100 characters)')
                description = ''
                self._continue()
                continue

        return description

    def _get_secret(self, secure_flag=True):
        secret = ''
        while not secret:
            print("\nIMPORTANT: Your secret phrase:")
            print("• Is case-sensitive")
            print("• Should be memorable but secure")
            print("• Will generate the same password every time")
            print("• Is never stored - only the hash is saved\n")

            if secure_flag:
                secret = getpass.getpass("Enter secret phrase (hidden): ")
            else:
                secret = input('Enter secret phrase: ')

            if not secret:
                print('Error: Secret phrase cannot be empty')
                self._continue()
                continue

            if secure_flag:
                secret2 = getpass.getpass("Confirm secret phrase (hidden): ")
            else:
                secret2 = input('Confirm secret phrase: ')

            if secret != secret2:
                print('Error: Secret phrases do not match')
                secret = ''
                self._continue()

        return secret

    def _get_password_length(self):
        while True:
            try:
                length = input('Enter password length (4-100): ')
                length = int(length)

                if length < 4:
                    print('Error: Minimum length is 4 characters')
                    continue
                elif length > 100:
                    print('Error: Maximum length is 100 characters')
                    continue

                return length

            except ValueError:
                print('Error: Please enter a valid number')
                self._continue()

    @staticmethod
    def _continue():
        input('\nPress Enter to continue... ')

    def run(self):
        self._show_logo()

        print("\n" + "=" * 60)
        print("⚠️  IMPORTANT: CLIPASSMAN v2.0.0")
        print("=" * 60)
        print("Breaking Changes:")
        print("• Login parameter removed - use only secret phrase")
        print("• All v1.x passwords are INVALID")
        print("• You must create NEW passwords")
        print("• Old password metadata cannot be migrated")
        print("=" * 60)
        print("\nIf you have old passwords:")
        print("1. Recover them using v1.x version")
        print("2. Generate new ones here with your secret phrases")
        print("3. Update your accounts with new passwords")
        print("=" * 60)

        confirm = input("\nPress Enter to continue or 'q' to quit: ")
        if confirm.lower() == 'q':
            return

        self.main_menu()
        self._show_footer()
