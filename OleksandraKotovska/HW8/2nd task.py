#Regular Expressions to check the validity of a password

import re 
user_pass = input("Enter your password: ")
error_message = "Wrong data! Your password has to contain at list"

#at list 1 letter between [a-z]
result_1 = re.findall("[a-z]", user_pass)
if result_1:
    print(result_1)
else:
    print(error_message + ' 1 letter between [a-z]')

#at list 1 letter between [A-Z]
result_2 = re.findall("[A-Z]", user_pass)
if result_2:
    print(result_2)
else:
    print(error_message + ' 1 letter between [A-Z]')

#at least 1 number between [0-9]
result_3 = re.findall("[0-9]", user_pass)
if result_3:
    print(result_3)
else:
    print(error_message + ' 1 number between [0-9]')

#at least 1 character from [$#@]
result_4 = re.findall("[$#@]", user_pass)
if result_4:
    print(result_4)
else:
    print(error_message + ' 1 character from [$#@]')

#minimum length 6 characters and maximum length 16 characters
result_5 = re.findall("^(?=.{6,16}$).*", user_pass)
if result_5:
    print(result_5)
else:
    print("Wrong data! Your password is too short or too long!")


if result_1 and result_2 and result_3 and result_4 and result_5:
    print("Your password is valid!")
else:
    print("Your password is invalid!")








