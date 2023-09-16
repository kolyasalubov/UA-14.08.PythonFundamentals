class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello! my name is {self.name}!"
    
    def species(cls):
        return "I am a species of Homosapiens."

    def arbtrary_message(message):
        return message
    

person = Human(input("Your name: "))
message = input("Type a message: ")

output = "\n".join([
    person.welcome(),
    person.species(),
    Human.arbtrary_message(message)
])

print(output)
