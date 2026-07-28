'''
Represents validators:
validates the input
'''

import re
class Validator:

    @staticmethod
    def is_not_empty(text):
        return len(text.strip()) > 0
            
    @staticmethod
    def has_no_spaces(text):
        return " " not in text
    
    @staticmethod
    def validate_website(website):
        pattern = r"^(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return bool(re.fullmatch(pattern, website))

    @staticmethod
    def validate_username(username):
        pass

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z1-9_]+@[a-zA-Z]+\.com$"
        return bool(re.fullmatch(pattern, email))

    @staticmethod
    def validate_password(password):
        return len(password.strip()) >= 8