# “WHAT IS YOUR NAME?“
# “HOW OLD ARE YOU?“
# “WHERE DO YOU LIVE?“

# “HELLO, (ANSWER(NAME))“.
# “YOUR AGE IS  (ANSWER(AGE))“.
# “YOU LIVE IN  (ANSWER(CITY))“.

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")

print(f"Hello, {name}.\n"
      f"Your age is {age}.\n"
      f"You live in {city}")