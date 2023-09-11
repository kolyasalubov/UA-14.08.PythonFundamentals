def bigger_number(num1: int, num2: int) -> int:
    """Function return the biggest number of two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2


number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
print(f"The bigger number is : ", bigger_number(number1, number2))
