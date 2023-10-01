days_dict = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday"
}


def input_number(days_dict_def: dict):
    while True:
        try:
            number = input("Enter your day of week:")
            if number not in days_dict_def:
                raise ValueError("Enter number between 1 and 7")
            return days_dict_def[number]
        except ValueError as e:
            print(e)


print(input_number(days_dict))
