password = input("Enter the password \n")

result = {True: 'Password is valid', False: 'The password must contain both lowercase and uppercase letters, numbers and symbols $#@'}

if 6 <= len(password) <= 16:

    import re

    regex = "[a-z]" and "[A-Z]" and "[0-9]" and "[$#@]"

    pattern = re.compile(regex)

    print(result[pattern.search(password) is not None])

else:
    print ("The password must contain from 6 to 16 characters")
