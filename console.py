'''
Represents menus and Ui
all the things that user will see
'''

from colorama import Fore, Style

class Console:
    def __init__(self):
        self.width = 120

    def show_header(self, text):
        print(Fore.LIGHTCYAN_EX + '=' * self.width)
        print(text.center(self.width))
        print('=' * self.width + Style.RESET_ALL)

    def show_sparator(self, text):
        print(Fore.LIGHTCYAN_EX + text * self.width + Style.RESET_ALL)

    def show_splitter(self, text):
        return Fore.LIGHTCYAN_EX + text + Style.RESET_ALL

    def show_main_menu(self):
        self.show_header("🔐 PASSWORD MANAGMENT")
        print(Fore.LIGHTWHITE_EX + "1. ➕ Add credential")
        print("2. 📋 Show credentials")
        print("3. 🗑 Delete credential")
        print("4. ✏️ Edit credential")
        print("0. 🚪 Exit" + Style.RESET_ALL)
        self.show_sparator('=')

    def show_credentials(self, credentials):
        self.show_header("📋 SHOW CREDENTIALS")
        print(f"{Fore.LIGHTWHITE_EX}{'ID'.center(5):<5}{self.show_splitter('|')}" \
              f"{Fore.LIGHTWHITE_EX}{'Website'.center(20):<20}{self.show_splitter('|')}" \
              f"{Fore.LIGHTWHITE_EX}{'Username'.center(20):<20}{self.show_splitter('|')}" \
              f"{Fore.LIGHTWHITE_EX}{'Email'.center(40):<40}{self.show_splitter('|')}" \
              f"{Fore.LIGHTWHITE_EX}{'Password'.center(30):<30}{self.show_splitter('|')}")
        self.show_sparator('-')

        for cred in credentials:
            print(f"{Fore.LIGHTWHITE_EX}{cred.cred_id:<5}{self.show_splitter('|')}" \
            f"{Fore.LIGHTWHITE_EX}{cred.website:<20}{self.show_splitter('|')}" \
            f"{Fore.LIGHTWHITE_EX}{cred.username:<20}{self.show_splitter('|')}" \
            f"{Fore.LIGHTWHITE_EX}{cred.email:<40}{self.show_splitter('|')}" \
            f"{Fore.LIGHTWHITE_EX}{cred.password:<30}{self.show_splitter('|')}")
            self.show_sparator('-')
    
        self.show_sparator('=')

    def show_success(self, text):
        print(Fore.LIGHTGREEN_EX + f"✅ {text}" + Style.RESET_ALL)

    def show_error(self, text):
        print(Fore.LIGHTRED_EX + f"✖️ {text}" + Style.RESET_ALL)

    def show_warning(self, text):
        print(Fore.LIGHTYELLOW_EX + f"⚠️ {text}" + Style.RESET_ALL)

    def show_empty(self, text):
        print(Fore.LIGHTBLUE_EX + f"📭 {text}" + Style.RESET_ALL)


    
