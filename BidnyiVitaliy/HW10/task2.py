# Create a class Human, everyone has a name, create a method in the 
# class that displays a welcome message to each person. Create a class method 
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.

class Human:

    name = ''

    def __init__(self, name):
        self.name = name
        

    def greet(self):
        print('Hello,', self.name)

    def species(self):
        return "Homosapiens" 

    @staticmethod
    def show_friends():
        print("Dog is Human's friend")   

#test
h = Human(name = 'Daniil')
h.greet()
print(h.species())
Human.show_friends()

