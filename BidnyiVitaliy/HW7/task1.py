# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

#Напишите функцию, которая возвращает наибольшее число из двух чисел.

def max(a, b):
    """returns the largest number of two numbers"""
    if a > b:
        return a
    else: 
        return b
    
# Tests    
print(max(2, 5))
print(max(22, 5))
print(max(2, 2))
print(max.__doc__)