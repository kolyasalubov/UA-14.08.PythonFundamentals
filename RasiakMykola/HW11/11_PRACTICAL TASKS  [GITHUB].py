
# 11 PRACTICAL TASKS / [GITHUB]

#Task 1
def task1_lesson_11():
    
    def age_(number):
        print(f"Your age is even") if (number%2 == 0) else print(f"Your age is odd")
        print('\n')
        
    while True:
        try:
            value = int(input('\nPlease enter your age: '))
            if value <=0:
                raise ValueError("You entered an incorrect age!.")
            elif value > 123:
                raise ValueError("I'm sorry, but that's very doubtful!.")  
        except ValueError as ve:
            print(ve)
            print("Please try again.")
        else:
            print("Thank you!")
            age_(value)
            break
        
#-----------------------------------------------------------------------------------------------

# Task 2   
def task2_lesson_11():
    
    choice = f"1 is Monday",\
             f"2 is Tuesday",\
             f"3 is Wednesday",\
             f"4 is Thursday",\
             f"5 is Friday",\
             f"6 is Saturday",\
             f"7 is Sunday"
    while True:
        try:
            for i in choice:
                print(i)
            value = int(input('\nPlease select the number that corresponds to the day of the week: '))
            if value > len(choice) or value <=0:
                raise ValueError(f"There is no such day in the week!")
            elif value <= len(choice) and value > 0:
                value -= 1
                print(choice[value])    
        except ValueError as ve:
            print(ve)
            print("Please try again.\n")
        else:
            print("Thank you for your choice!")
            break

task1_lesson_11()
task2_lesson_11()

    
     
 
