# Task 2 "Human class"
class Human():
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        return print(f"Welcome {self.name}!")
    
    
    
class Homosapiens(Human):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def welcome_homo(self):
        return print(f"{self.name.title()} you are a Homosapiens!")

    @staticmethod
    def some_static_message():
        print("Congratulations! You are human!")


if __name__ == "__main__":
    andy = Homosapiens("Andy")
    andy.welcome()
    andy.welcome_homo()
    andy.some_static_message()