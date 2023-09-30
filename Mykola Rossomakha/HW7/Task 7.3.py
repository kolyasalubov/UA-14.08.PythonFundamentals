def calculate_value(string):
    """
    Функція повертає кількість літер у рядку у формі словника.

    """
    number_of_characters = {}
    for letter in string:
        # Перевіряємо, чи літера вже є у словнику
        if letter in number_of_characters:
            number_of_characters[letter] += 1
        else:
            number_of_characters[letter] = 1
    return number_of_characters

input_string = input("Введіть рядок: ").lower()
print(calculate_value.__doc__)
print(calculate_value(input_string))
