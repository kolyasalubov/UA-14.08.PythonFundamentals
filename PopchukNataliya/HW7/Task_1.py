# Function that return largest number of two
def find_largest_number(num1, num2):
    """Returns the largest number of two input numbers"""
    if num1 > num2:
        return num1
    else:
        return num2


num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
result = find_largest_number(num1, num2)
print("The largest number is:", result)
