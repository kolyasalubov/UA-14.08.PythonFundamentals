################ 1st task #######################

def main():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        elif age == 0:
           raise ValueError("Age has to be higher than 0") 
        elif age % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError as e:
        return e
    except Exception:
        return "Other errors"

print(main())


################### 2nd task ####################################


# def day(number):
#     week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
#     if number < 1 or number > 7:
#         raise ValueError("Please enter a number between 1 and 7.")
#     return week[number - 1]

# def checking():
#     try:
#         n = int(input("Enter the numbers from 1 to 7 to know the day: "))
#         days = day(n)
#         print(days)
#     except ValueError as e:
#         print(e)
#     except Exception:
#         print('Other errors')


# checking()
