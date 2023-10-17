def your_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be so old")

    if age % 2 == 0:
        return "even"
    if age % 2 == 1:
        return "odd"

try:
    age = int(input("Enter your age: "))
    result = your_age(age)
    print(f"Your age is {result}.")
except ValueError as e:
    print(f"Error: {e}")
