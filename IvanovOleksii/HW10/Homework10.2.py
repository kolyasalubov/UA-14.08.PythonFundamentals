class Human:
    homosapiens = 'Homosapiens'

    def __init__(self, username):
        self.username = username

    def welcome_message(self):
        return f'Welcome, {self.username}!'

    @classmethod
    def sort(cls):
        return cls.homosapiens

    @staticmethod
    def message():
        message = '<Hello_World>'
        return message


# Test
exp1 = input('Enter your name: ')
exp1_1 = Human(exp1)
print(exp1_1.welcome_message())
print(exp1_1.sort())
print(exp1_1.message())
