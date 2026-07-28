'''
Represents a single credential stored in the password manager.
'''
from console import Console

console = Console() 
class Credential:
    def __init__(self, cred_id, website, username, email, password):
        self.cred_id = cred_id
        self.website = website
        self.username = username
        self.email = email
        self.password = password

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
    
    def to_dict(self):
        return {
            "cred_id": self.cred_id,
            "website": self.website,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["cred_id"],
            data["website"],
            data["username"],
            data["email"],
            data["password"]
        )