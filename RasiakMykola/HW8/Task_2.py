import re


def validation_1(password_user):
    
    list_check = []
    if len(password_user) < 6 or len(password_user) > 16:
        actions = 2
    else:
        actions = 1
        match actions:
            case 1:
                list_check.append(bool(re.search("[a-z]", password_user))) 
                list_check.append(bool(re.search("[A-Z]", password_user)))
                list_check.append(bool(re.search("[0-9]", password_user))) 
                list_check.append(bool(re.search("[$#@]", password_user))) 
                return all(list_check)   
            case 2:
                return False

              
password_user = input("\nEnter your password: ")

print("The password is valid.") if validation_1(password_user)else print("The password is not valid.") 



