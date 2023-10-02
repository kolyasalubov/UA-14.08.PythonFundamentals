class Human:
    viewes  = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, my name is {self.name}. Welcome!"

    @classmethod
    def get_viewes(cls):
        return cls.viewes

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

person1_name = input("Enter your name:")
person1 = Human(person1_name)
person2_name = input("Enter your name:")
person2 = Human(person2_name)

print(person1.welcome_message())  
print(person2.welcome_message())
print(Human.get_viewes())     
print(Human.arbitrary_message())