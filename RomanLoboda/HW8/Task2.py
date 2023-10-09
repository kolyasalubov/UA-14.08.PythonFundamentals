import re


def validation(user_password):
    """

    Args:
        user_password must be:
        - Length between 6 and 16 characters
        - At least one lowercase letter [a-z]
        - At least one uppercase letter [A-Z]
        - At least one number [0-9]
        - At least one character from [$#@]

    Returns:
        the validation is successful if the password is valid
        or the validation is failed
    """
    condition_1 = re.search("[A-Z]", user_password)
    condition_2 = re.search("[a-z]", user_password)
    condition_3 = re.search("[0-9]", user_password)
    condition_4 = re.search("[$#@]", user_password)
    condition_5 = 6 <= len(user_password) <= 16

    if condition_1 and condition_2 and condition_3 and condition_4 and condition_5:
        print("the validation is successful")
    else:
        print("the validation is failed ")


validation((input("Enter password : ")))
