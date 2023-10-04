def day_of_week(number):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if number < 1 or number > 7:
        return "\nError. You need to enter a number from 1 to 7 to get the day of the week!!!"

    return days_of_week[number - 1]


try:
    user_input = input("Enter a number from 1 to 7 to get the day of the week: ")
    user_input = int(user_input)

    day = day_of_week(user_input)
    print(f"The day of the week is: {day}")
except ValueError:
    print("Invalid input. Please enter a valid number between 1 and 7.")
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")