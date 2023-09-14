# Script that checks the login that the user enters

correct_login = "First"
while True:
    user_login = input("Enter your login: ")
    if user_login == correct_login:
        print("Welcome, user.")
        break
    else:
        print("Error:Invalid login. Please try again.")
