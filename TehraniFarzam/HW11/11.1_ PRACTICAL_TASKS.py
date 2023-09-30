def odd_oreven_age():
    try:
        age = int(input("How old are you? "))
        if age < 0:
            raise ValueError("Age can not be negative.")
        odd_even = lambda num: "Even" if num % 2 == 0 else "Odd"
        result = odd_even(age)
        print(f"your age is {result} number.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid input!")


odd_oreven_age()
