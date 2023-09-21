def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if number < 1 or number > 7:
        return "Invalid input. Enter a number from 1 to 7."

    return days[number - 1]


def main():
    try:
        number = int(input("Enter a number from 1 to 7: "))
        day = get_day_of_week(number)
        print(f"Day of the week: {day}")
    except ValueError:
        print("Error: Enter a valid number from 1 to 7.")


if __name__ == "__main__":
    main()
