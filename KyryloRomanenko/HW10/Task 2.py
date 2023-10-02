class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome {self.name}")


class Homosapiens(Human):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def static_print():
        print(f"You are a Homosapiens")


if __name__ == '__main__':
    human = Homosapiens(input("Enter you name:"))
    human.welcome_message()
    human.static_print()
