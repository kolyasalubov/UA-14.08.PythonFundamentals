login = "First"

while True:
    input_login = input("LOGIN: ").capitalize()

    if input_login == login:
        print("Hello, you are logged in.")
        break
    else:
        print("Login failed, try again!")