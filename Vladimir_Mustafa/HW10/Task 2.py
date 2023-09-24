class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'am {self.name}!"

    def species_info(self):
        return "I belong to the Homosapiens mind."

    @staticmethod
    def random_message():
        return "This is a random message."

person1 = Human("Vova")
print(person1.greet())
print(person1.species_info())

random_msg = Human.random_message()
print(random_msg) 
