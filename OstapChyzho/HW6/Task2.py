check_login = input("Please enter your login:")
login = "First"

print(check_login)

while True:
    if check_login == login:
        print("Congratulations!")
        break
    else:
        print(input("Incorrect login.Please try agin:"))
        