# password validity with string function
def password_validity_sring(password, min_char_in_password = 6, max_char_in_password = 16):
    """Password validity
    with string function
    """
    chars_in_password = "$#@"

    char_count = False
    letter_upper = False
    letter_lower = False
    digit = False
    char_in = False

    if min_char_in_password <= len(password) and len(password) <= max_char_in_password:
        char_count = True
    
    for i in password:
        if i.isdigit():
            digit = True
        if i.isalpha() and i.isupper():
            letter_upper = True
        if i.isalpha() and i.islower():
            letter_lower = True
        if i in chars_in_password:
            char_in = True

    if char_count and digit and letter_upper and letter_lower and char_in:
        return True
    return False

print(password_validity_sring('012d45F78@123456777'))



# password validity with RE library
def password_validity_re(password, min_char_in_password = 6, max_char_in_password = 16):
    """Password validity
    with RE library
    """

    import re
    pattern_string = r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*[$#@].*)[0-9a-zA-Z$#@]{' + str(min_char_in_password) + "," + str(max_char_in_password) + "}$"
    pattern = re.compile(pattern_string)  
    
    return bool(pattern.match(password))

print(password_validity_re('012d45F78@123456'))