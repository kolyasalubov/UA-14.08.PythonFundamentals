def largest_number(num1: float, num2: float) -> float:
    """
    :param num1: first number
    :param num2: second number

    :return: return the largest number
    """

    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


x = largest_number(2.124124,1.13124125)
print(x)
