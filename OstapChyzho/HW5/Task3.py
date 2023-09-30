num = input("Enter a positive number: ")

if num.isdigit():
    num = int(num)
    if num < 0:
        print("negative number")
    elif num == 0 or num == 1:
        print("Factorial of", num, "is:", 1)
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        print("Factorial of", num, "is:", result)
else:
    print("Please enter a valid positive number.")
