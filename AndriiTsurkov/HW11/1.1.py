class Age():
    def __init__(self) -> None:
        age = input("Please enter your age: ")
        self.main(self.validation(age))

    def validation(self, age: str) -> int:
        try:
            age = int(age)
        except ValueError as e:
            print(f"Error: You have entered not nuber! And we have error {e}")
            exit(0)
        return age
    
    def main(self, age: int) -> None:
        try:
            if age > 0:
                if age % 2 == 0: 
                    print(f"Yor age {age} is even.")
                else:
                    print(f"Yor age {age} is odd.")
            else:
                raise ValueError(f"Your age {age} is less than zero.")
        except ValueError as e:
            print(e)

human = Age()