def largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = largest_number(num1, num2)
print(f"The largest number is {result}.")