class Day_of_week():
    def __init__(self, day: str) -> None:
        self.main(self.check(day))

    def check(self, day: str) -> int:
        try:
            day = int(day)
        except ValueError as er:
            print("Error:", er)
            exit(0)
        return day

    def main(self, day: int) -> None:
        match day:
            case 1:
                print(f"{day} is Monday.")
            case 2:
                print(f"{day} is Tuesday.")
            case 3:
                print(f"{day} is Wednesday.")
            case 4:
                print(f"{day} is Thursday.")
            case 5:
                print(f"{day} is Friday.")
            case 6:
                print(f"{day} is Saturday.")
            case 7:
                print(f"{day} is Sunday.")
            case _:
                print("Your number is not included in the days of the week.")
            
Day_of_week(input("Plese enter number of day from week: "))
