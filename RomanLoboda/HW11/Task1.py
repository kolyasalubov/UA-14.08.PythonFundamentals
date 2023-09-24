class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def age_valid(age):
    if age <= 0:
        raise MyError("Your age should be more then 0")
    elif age % 2 == 0:
        print(f"Your age {age} is even")
    else:
        print(f"Your age {age} is odd")


try:
    age_valid(int(input("Enter your age : ")))
except MyError as e:
    print(e)
