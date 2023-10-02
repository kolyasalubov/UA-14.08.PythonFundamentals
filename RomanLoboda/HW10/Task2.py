class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello {self.name}"

    @classmethod
    def dis_species(cls):
        return f"Homosapiens"

    @staticmethod
    def my_message():
        return "Everything is good"


name = Human(input("Enter your name : "))
print(name)
print(Human.dis_species())
print(Human.my_message())
