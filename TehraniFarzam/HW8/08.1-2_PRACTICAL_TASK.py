import re

def is_valid_password(password):
    """
    Validate a password based on the following criteria:
    - Length between 6 and 16 characters
    - At least one lowercase letter [a-z]
    - At least one uppercase letter [A-Z]
    - At least one number [0-9]
    - At least one character from [$#@]
    
    Returns:
    - True if the password is valid, False otherwise.
    """

    if not (6 <= len(password) <= 16):
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

