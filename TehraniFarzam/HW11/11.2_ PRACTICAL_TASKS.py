def corresponding_day():
    daysOfWeek = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 
                  4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    try:
        input_day = int(input("Enter a number and I will tell you what day is today: "))
        
        if 1 <= input_day <= 7:
            what_day = lambda dict, key: dict[key] if key in dict else "Invalid input"
            result = what_day(daysOfWeek, input_day)
            print(F"Today is {result}")
        else:
            print("Enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input")


corresponding_day()
        