'''
Main menu of the program
'''
from colorama import Fore, Style

from console import Console
from credential import Credential
from password_manager import PasswordManager
from validator import Validator
from crypto_utils import Key, CryptoUtils

console = Console()
manager = PasswordManager()

key = Key.load_key()
if key is None:
    key = Key.generate_key()
    Key.save_key(key)

crypto = CryptoUtils(key)

Credential.set_crypto(crypto)

def get_user_choice(text):
    try:
        choice = int(input(text))
    except ValueError:
        console.show_warning("Invalid input!")
        return -1
    return choice

def get_empty():
    if manager.empty_list():
        console.show_empty("Credential list is empty!")
        return True
    return False
    
def mainmenu():
    while True:
        console.show_main_menu()
        choice = get_user_choice("Enter your choice: ")
        if choice == 1:
            console.show_header("➕ ADD CREDENTIAL")
            while True:
                website = input("Enter website: ")
                if not Validator.has_no_spaces(website):
                    console.show_error("Website can't have space!")
                    continue
                if not Validator.is_not_empty(website):
                    console.show_error("Input can't be empty!")
                    continue
                if not Validator.validate_website(website):
                    console.show_error("Invalid website!")
                    continue
                break
            while True:
                username = input("Enter username (optional): ")
                if username == "":
                    break
                if not Validator.has_no_spaces(username):
                    console.show_error("Username can't have space!")
                    continue
                break
            while True:
                email = input("Enter email (optional): ")
                if email == "":
                    break
                if not Validator.has_no_spaces(email):
                    console.show_error("email can't have space!")
                    continue
                if not Validator.validate_email(email):
                    console.show_error("Invalid email!")
                    continue
                break
            if username == "" and email == "":
                console.show_error("You must enter at least username or email!")
                continue

            while True:
                password = input("Enter password: ")
                if not Validator.has_no_spaces(password):
                    console.show_error("Password can't have space!")
                    continue
                if not Validator.is_not_empty(password):
                    console.show_warning("Input can't be empty!")
                    continue
                if not Validator.validate_password(password):
                    console.show_error("Password should be at least 8 character!")
                    continue
                break
            cred_id = None
            credential = Credential(cred_id, website, username, email, password)
            manager.add_credential(credential)
            console.show_success("Credential Added!")
            console.show_sparator('=')
        elif choice == 2:
            credentials = manager.show_credentials()
            if not credentials:
                console.show_error("No credential found!")
            else: 
                console.show_credentials(credentials)
        elif choice == 3:
            if get_empty():
                continue
            console.show_header("🗑 DELETE CREDENTIAL")
            while True:
                delete = False
                search = get_user_choice("\nEnter credential ID: ")
                credential = manager.search_by_id(search)
                if credential: 
                    while True:
                        confirm = input(f"Deleting \"{credential.website}\" credential. Are you sure? (y/n): ").lower()
                        if confirm == 'y':
                            manager.remove_credential(credential)
                            console.show_success(f"Credential: {credential.website} deleted successfully!")
                            delete = True
                            break
                        elif confirm == 'n':
                            console.show_error("Deleting process canceled!")
                            delete = True
                            break
                        console.show_warning("Invlaid input!")
                        continue
                else:
                    console.show_error("No credential found!")
                    break
                if delete is True:
                    break
        elif choice == 4:
            if get_empty():
                continue
            console.show_header("✏️ EDIT CREDENTIAL")
            while True:
                search = get_user_choice("\nEnter credential ID: ")
                searched = manager.search_by_id(search)
                if searched:
                    while True:
                        new_website = input("Enter new website (leave blank to keep current): ")
                        if new_website == "":
                            break
                        if not Validator.has_no_spaces(new_website):
                            console.show_error("Website can't have space!")
                            continue
                        if not Validator.validate_website(new_website):
                            console.show_error("Invalid website!")
                            continue
                        break
                    while True:
                        new_username = input("Enter new username (leave blank to keep current): ")
                        if new_username == "":
                            break
                        if not Validator.has_no_spaces(new_username):
                            console.show_error("Username can't have space!")
                            continue
                        break
                    while True:
                        new_email = input("Enter new email (leave blank to keep current): ")
                        if new_email == "":
                            break
                        if not Validator.has_no_spaces(new_email):
                            console.show_error("email can't have space!")
                            continue
                        if not Validator.validate_email(new_email):
                            console.show_error("Invalid email!")
                            continue
                        break
                    while True:
                        new_password = input("Enter new password (leave blank to keep current): ")
                        if new_password == "":
                            break
                        if not Validator.has_no_spaces(new_password):
                            console.show_error("Password can't have space!")
                            continue
                        if not Validator.validate_password(new_password):
                            console.show_error("Password should be at least 8 character!")
                            continue
                        break
                    
                    if manager.edit_credential(search, new_website, new_username, new_email, new_password):
                        console.show_success("Credential edited successfully!")
                    else:
                        console.show_warning("Nothing changed!")
                    break
                else:
                    console.show_error("No credential founded!")
                    break            
        elif choice == 0:
            break
        elif choice == -1:
            continue
        else:
            console.show_warning("Invalid choice!")
            
if __name__ == "__main__":
    mainmenu()

