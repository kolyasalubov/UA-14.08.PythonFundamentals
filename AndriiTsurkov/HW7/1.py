def largest_number(first_number: str, second_number: str):
    
    if first_number.isdecimal() and second_number.isdecimal():
        first_number = int(first_number)
        second_number = int(second_number)

        if first_number > second_number:
            return first_number
        elif second_number > first_number:
            return second_number
        else:
            return f"The numbers {first_number} and {second_number} are equal" 
    else:
        return 'Error! You have enter not a digit.'
    
     
first_number  = input("Plese enter first number: ")
second_number = input("Plese enter second number: ")

print(largest_number(first_number, second_number))
