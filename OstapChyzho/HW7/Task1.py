def largest(num1,num2):
    """
    This function return the largest of two numbers
    """
    if num1 > num2:
        return num1
    else:
        return num2
while True:
    try:
        result = largest(float(input("first num:")),float(input("Second num:")))
        print("the largest number is:", result)
    except:
        print("Its not a number")