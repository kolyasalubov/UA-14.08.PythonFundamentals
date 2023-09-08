def largest_number(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number
    else:
        return f"The numbers {first_number} and {second_number} are equal" 
     
first_number  = input("Plese enter first number: ")
second_number = input("Plese enter second number: ")

print(largest_number(first_number, second_number))
