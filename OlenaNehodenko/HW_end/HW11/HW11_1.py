def user_age():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age % 2 == 0:
            print(f"You entered an even age: {age}")
        else:
            print(f"You entered an odd age: {age}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    user_age()