# Запит користувача на введення температури в градусах Цельсія
celsius = float(input("Введіть температуру в градусах Цельсія: "))

# Перевірка, чи введена температура нижче абсолютного нуля
if celsius < -273.15:
    # Якщо так, вивід повідомлення про помилку
    print("Помилка: Температура нижче абсолютного нуля (-273.15°C)")
else:
    # Якщо температура введена коректно, проведення перетворення
    fahrenheit = (celsius * 9/5) + 32
    # Виведення результату
    print(f"{celsius}°C дорівнює {fahrenheit}°F")