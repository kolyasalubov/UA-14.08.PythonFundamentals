# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
#1
import re

#2
while True:
  #3
  user_input = input("Enter a password : ")
  is_valid = False

  if (len(user_input)<6 or len(user_input)>16):
    #4
    print("Not valid! Total characters should be between 6 and 16")
    continue
  elif not re.search("[a-z]",user_input, re.IGNORECASE):
    #6
    print("Not valid! It should contain one letter between [a-z] and 1 letter between [A-Z]")
    continue
  elif not re.search("[0-9]",user_input):
    #7
    print("Not valid! It should contain one digit between [0-9]")
    continue
  elif not re.search("[$#@]",user_input):
    #8
    print("Not valid! It should contain at least one letter in [$#@]")
    continue
  elif re.search("[\s]",user_input):
    #9
    print("Not valid! It should not contain any space")
    continue
  else:
    #10
    is_valid = True
    break

#11
if(is_valid):
  print("Password is valid")