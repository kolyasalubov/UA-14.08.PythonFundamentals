def character_positions(wrd):
    """
    calculate the number of characters
    """
    wrd = wrd.lower() 
    char_positions = {}

    for i, char in enumerate(wrd, start = 1):
        if char:
            char_positions[i] = char

    return char_positions

word = input("Enter a string: ")
result = character_positions(word)
print("Character positions:", result)