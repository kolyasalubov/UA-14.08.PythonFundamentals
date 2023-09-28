class Day_of_week():
    def __init__(self, day: str) -> None:
        self.days_of_week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}    
        self.main(self.check(day))

    def check(self, day: str) -> int:
        try:
            day = int(day)
        except ValueError as er:
            print("Error:", er)
            exit(0)
        return day

    def main(self, day: int) -> None:
        if day < 0 or day > 7:
            print("Your number not included in the days of the week.")
        else:
            print(f"{day} is {self.days_of_week.get(day)}.")


Day_of_week(input("Plese enter number of day from week: "))


