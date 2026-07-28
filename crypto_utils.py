from cryptography.fernet import Fernet

class Key:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def save_key(key, filename="key.key"):
        try:
            with open(filename, "wb") as f:
                f.write(key)
            return True
        except Exception as e:
            print(f"Error saving key: {e}")
            return False       

    @staticmethod
    def load_key(filename="key.key"):
        try:
           with open(filename, "rb") as f:
               return f.read()
        except FileNotFoundError:
           return None
        except Exception as e:
            print(f"Error loading key: {e}")
            return None
    
class CryptoUtils:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt_password(self, password):
        if not password:
            return ""
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        if not encrypted_password:
            return ""
        return self.cipher.decrypt(encrypted_password.encode()).decode()