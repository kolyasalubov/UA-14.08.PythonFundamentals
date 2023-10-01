
# 10.2 PRACTICAL TASKS / [GITHUB]

# Task 2
class Human:
    
    sentence  = r"You belong to the species 'Homosapiens'"
 
    def __init__(self, name):
        self.name = name

    def the_welcome_message(self):
        print(f"Welcome, {self.name}!\n")

    @classmethod
    def Homosapiens(cls):
        return f"{cls.sentence}"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."



person = Human(input ("\nWhat is your name: "))


person.the_welcome_message()  
print(person.Homosapiens(), end='. ')  
print(Human.arbitrary_message())  
