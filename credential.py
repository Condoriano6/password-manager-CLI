'''
Represents a single credential stored in the password manager.
'''

class Credential:
    def __init__(self, cred_id, website, username, email, password):
        self.cred_id = cred_id
        self.website = website
        self.username = username
        self.email = email
        self.password = password
