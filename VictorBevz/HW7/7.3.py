def count_characters(input_string):
    character_count = {}

    for char in input_string:
        character_count[char] = character_count.get(char, 0) + 1

    return character_count

input_string = input("Input a word:")
result = count_characters(input_string)
print (f"The result is {result}")