def input_age():
    while True:
        try:
            age = int(input("Enter you age:"))
            if age <= 0:
                raise ValueError("Your Age should be more that 0")
            return age
        except ValueError as e:
            print(e)


def check_even_ood(age: int):
    if age % 2 == 0:
        print(f"Your age {age} are even")
    else:
        print(f"Your age {age} are odd")


if __name__ == '__main__':
    check_even_ood(input_age())
