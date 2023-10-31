import re


def is_valid_password(password):
    # Check the length of the password
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least 1 lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least 1 uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least 1 digit
    if not re.search(r'[0-9]', password):
        return False

    # Check for at least 1 special character from [S#@]
    if not re.search(r'[S#@]', password):
        return False

    return True


# Input password from the user
password = input("Enter a password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
