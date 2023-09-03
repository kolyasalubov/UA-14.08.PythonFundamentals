input_login = input("Enter login : ")
counter = 0

while True:
    if input_login == "First":
        print("Hello")
        break
    elif counter == 5:
        print("Your login is not correct, try again after 15 minutes")
        break
    else:
        print("Your login is not correct, try again")
        input_login = input("Enter login again: ")
    counter += 1
