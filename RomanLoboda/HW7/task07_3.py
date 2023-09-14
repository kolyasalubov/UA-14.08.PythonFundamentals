def calculate_value(string: str) -> dict:
    """function return the number of letter in the string"""
    number_of_character = {}
    for letter in string:
        number_of_character[letter] = string.count(letter)
    return number_of_character


input_string = input("Enter a string : ").lower()
print(calculate_value.__doc__)
print(calculate_value(input_string))

