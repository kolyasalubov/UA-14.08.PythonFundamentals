import re


def input_password():
    return input("Write your passord and press Enter for checking:\n")


def check_password(password):
    status = 0

    while status < 5:
        print(status)
        if len(re.findall("[a-z]", password)) > 0:
            status_a_z = 1

        else:
            print("Your passowrd should has minimum 1 letter a-z in lower register")
            password = input("Write your passord and press Enter for checking:\n")
            continue

        if len(re.findall("[A-Z]", password)) > 0:
            status_upper_a_z = 1
        else:
            print("Your passowrd should has minimum 1 letter A-Z in Upper register")
            password = input("Write your passord and press Enter for checking:\n")
            continue

        if len(re.findall("[0-9]", password)) > 0:
            status_1_9 = 1
        else:
            print("Your passowrd should has minimum 1 number 0-9 ")
            password = input("Write your passord and press Enter for checking:\n")
            continue

        if len(password) <= 16:
            status_max = 1
        else:
            print("Your passowrd so long. Use maximum 16 simbols")
            password = input("Write your passord and press Enter for checking:\n")
            continue

        if len(password) >= 6:
            status_min = 1
        else:
            print("Your passowrd so short. Use maximum 6 simbols")
            password = input("Write your passord and press Enter for checking:\n")
            continue
        status = status_a_z + status_upper_a_z + status_1_9 + status_min + status_max

    else:
        print("Your passwir is correct")
        status = 5


def main():
    password = input_password()
    check_password(password)


if __name__ == '__main__':
    main()
