def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "Even age"
    else:
        return "Odd age"

def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(f"Your age: {age}")
        print(f"Result of checking: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
