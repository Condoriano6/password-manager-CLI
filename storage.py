'''
save & load files
'''
import json

from credential import Credential

def load_credentials():
    try:
        with open("credentials.json", 'r', encoding="utf-8") as f:
            data = json.load(f)
            credentials = [Credential.from_dict(item) for item in data]
            return credentials
    except FileNotFoundError:
        return []
    except Exception as e:  
        print(f"Unkmown Error: {e}")
        return []

def save_credentials(credentials):
    try:
        with open("credentials.json", 'w', encoding="utf-8") as f:
            data = [credential.to_dict() for credential in credentials]
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:  
        print(f"Unkmown Error: {e}")
        return -1
