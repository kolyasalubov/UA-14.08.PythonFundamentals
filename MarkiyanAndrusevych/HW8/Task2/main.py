import re

def valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"

    if re.match(pattern, password):
        return True
    else:
        return False

password = input("Create a password: \n")

if valid_password(password):
    print("Thank you! Your password is valid :)")
else:
    print("Invalid password :( Please try again!")