class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        for key, value in self.options.items():
            print(f"{key}. {value}")

    @staticmethod
    def choose_option():
        choice = input("Select login: ")
        return choice


class MultiLevelMenu:
    def __init__(self):
        self.main_menu = Menu("Main menu", {
            "1": "Password 1",
            "2": "Password 2",
            "3": "Password 3",
        })

        self.submenu = Menu("Slave menu", {
            "1": "Get password",
            "2": "Delete",
            "3": "Back",
            "4": "Exit"
        })

    def run(self):
        while True:
            self.main_menu.display()
            choice = self.main_menu.choose_option()

            if choice == "1":
                self.submenu_display()
            elif choice == "2":
                print("Вы выбрали Пункт 2")
            elif choice == "3":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def submenu_display(self):
        while True:
            self.submenu.display()
            choice = self.submenu.choose_option()

            if choice == "1":
                print("Вы выбрали Получить")
            elif choice == "2":
                print("Вы выбрали Удалить")
            elif choice == "3":
                break
            elif choice == "4":
                print("До свидания!")
                exit()
            else:
                print("Неверный выбор. Попробуйте снова.")


class Menu:

    @staticmethod
    def display_sub_menu():
        print("1. Get password")
        print("2. Delete case")
        print("3. Back")
        print("4. Exit")

    @staticmethod
    def main_menu(password_manager):
        while True:
            for login in password_manager.passwords.keys():
                print(login)
            print("0. Add smart password")

            choice = input("Select login or action: ")

            if choice == "0":
                password_manager.add_password()
            elif choice in password_manager.passwords:
                while True:
                    print("\nLogin selected:", choice)
                    Menu.display_sub_menu()
                    action = input("Choose an action: ")

                    if action == "1":
                        password_manager.get_password(choice)
                    elif action == "2":
                        password_manager.delete_password(choice)
                    elif action == "3":
                        break
                    elif action == "4":
                        print("Exit.")
                        return
                    else:
                        print("Wrong option.")
            else:
                print("Login not found.")
