import re

def validate_password(password):
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
password = input("Enter a password, please: ")
# Validate the password
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")