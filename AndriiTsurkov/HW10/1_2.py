# Task 2 "Human class"

class Human():
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        return print(f"Welcome {self.name}!")
    
    def type_of_human(self):
        return print(f"{self.name.title()} you are a Homosapiens")

    @staticmethod
    def random_message():
        print("Congratulations! You are human!")

#class

andy = Human("Andy")
andy.welcome()
andy.type_of_human()
Human.random_message()
