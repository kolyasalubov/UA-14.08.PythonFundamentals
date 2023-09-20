# Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

# Напишите функцию, которая вычисляет количество символов
# включенн в данную строку
# • input: «hello»
# • output: {"h":1, "e":1, "l":2, "o":1}

def num_of_chars(str):
    output = dict()
    for l in str:
        if l in output:
            output[l] = output[l] + 1
        else:
            output[l] = 1
    return output
# Tests
print(num_of_chars("hello"))
