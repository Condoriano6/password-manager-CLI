'''
Represents the actions that user can do on credentials
'''

from colorama import Fore, Style

from credential import Credential
from storage import load_credentials, save_credentials
class PasswordManager:
    def __init__(self):
        self.credentials = load_credentials()
        if self.credentials:
            self.next_id = max(credential.cred_id for credential in self.credentials) + 1
        else:
            self.next_id = 1

    def empty_list(self):
        return not self.credentials

    def search_by_id(self, search):
        for credential in self.credentials:
            if credential.cred_id == search:
                return credential
        return None
    
    def add_credential(self, credential):
        credential.cred_id = self.next_id
        self.credentials.append(credential)
        self.next_id += 1
        save_credentials(self.credentials)

    def show_credentials(self):
        return self.credentials
    
    def remove_credential(self, credential):
        self.credentials.remove(credential)
        save_credentials(self.credentials)

    def edit_credential(self, cred_id, new_website, new_username, new_email, new_password):
        credential = self.search_by_id(cred_id)
        if not credential:
            return False
        
        changed = credential.edit(new_website, new_username, new_email, new_password)
        
        if changed:
            save_credentials(self.credentials)
            return True
        return False
    def sort_credential(self):
        pass

    def filter_credential(self):
        pass
