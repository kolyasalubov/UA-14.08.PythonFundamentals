# Task 2
class Human:
    def __int__(self, name):
        self.name = name

    def input(self):
        self.name = str(input("Enter your name: "))

    def welcome_message(self):
        print(f"Welcome {self.name} !!!")

    @classmethod
    def class_method(cls):
        return "Homo sapiens, (Latin: “wise man”) the species to which all modern human beings belong."

    @staticmethod
    def static_method():
        return "Goodbye"

human = Human()
human.input()
human.welcome_message()
print(human.class_method())
print(human.static_method())