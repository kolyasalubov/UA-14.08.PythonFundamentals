def get_day(number):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= number <= 7:
        return days_of_week[number - 1]
    else:
        return "Invalid input. Please enter a number between 1 and 7."

if __name__ == "__main__":
    try:
        user_input = input("Enter a number (1-7) to get the day of the week: ")
        number = int(user_input)
        day_of_week = get_day(number)
        print(f"The day of the week {number} is {day_of_week}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")