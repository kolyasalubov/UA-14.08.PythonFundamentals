# 8.2 task
def password(user_password):
    special_characters = ['S', '@', '#']
    val = True

    if len(user_password) < 6:
        print("Minimum length is 6 characters")
        val = False

    if len(user_password) > 16:
        print("Maximum length is 16 characters")
        val = False

    if not any(char.isdigit for char in user_password):
        print("Password require minimum 1 number")
        val = False

    if not any(char.isupper for char in user_password):
        print("Password must have at least one uppercase letter")
        val = False

    if not any(char.islower for char in user_password):
        print("Password must have at least on lowercase letter")
        val = False

    if not any(char in special_characters for char in user_password):
        print("Password must contain at least one character S or @ or #")
        val = False
    
    if val:
        return val

user_input = input("Please enter your password: ")
result = password(user_input)

if result:
    print("Password is accepted")
else:
    print("Please check the requirements")