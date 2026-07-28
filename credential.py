'''
Represents a single credential stored in the password manager.
'''
from console import Console
from crypto_utils import CryptoUtils

console = Console() 
class Credential:
    crypto = None

    @classmethod
    def set_crypto(cls, crypto):
        cls.crypto = crypto

    def __init__(self, cred_id, website, username, email, password):
        self.cred_id = cred_id
        self.website = website
        self.username = username
        self.email = email
        self._password = password

    def edit(self, website, username, email, password):
        changed = False

        if website:
            self.website = website
            changed = True
        if username:
            self.username = username
            changed = True
        if email:
            self.email = email
            changed = True
        if password:
            self.password = password
            changed = True
        return changed

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def to_dict(self):
        if self.crypto and self._password:
            encrypted_password = self.crypto.encrypt_password(self._password)
        else:
            encrypted_password = self._password

        return {
            "cred_id": self.cred_id,
            "website": self.website,
            "username": self.username,
            "email": self.email,
            "password": encrypted_password
        }

    @classmethod
    def from_dict(cls, data):
        password = data["password"]

        if cls.crypto and password:
            try:
                password = cls.crypto.decrypt_password(password)
            except:
                pass
            
        return cls(
            data["cred_id"],
            data["website"],
            data["username"],
            data["email"],
            password
        )