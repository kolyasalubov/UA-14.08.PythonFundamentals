def count_characters(input_string):
    """
    This function counts the number of characters in the input string.

    Parameters:
        input_string (str).

    Returns:
        dict: Keys are characters and values are number of characters.
    """
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


input_string = str(input("Please enter a phrase, or word: "))
result = count_characters(input_string)
print(f"The result is: {result}.")