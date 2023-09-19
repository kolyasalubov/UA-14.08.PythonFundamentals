import re

def validate(password):
    if not 6 <= len(password) <= 16:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True
password = input("Enter your password here ->")

if validate(password):
    print("Password is OK")
else:
    print("Invalid password")