class Human:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        return f"My name is {self.name}"
    def species(sp):
        return "I'm a Homosapiens"
    def arb_mess(message):
        return message
    
human = Human(input("Input your name->"))
message = input("Input your message->")

out = "\n".join([human.welcome(), human.species(), Human.arb_mess(message)])

print(out) 