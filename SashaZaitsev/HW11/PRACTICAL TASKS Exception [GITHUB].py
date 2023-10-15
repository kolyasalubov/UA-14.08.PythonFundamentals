#1
def check_age(age):
    if age < 0:
        raise ValueError("Вік вказанно некореткно!")
    elif age % 2 == 0:
        return "Парне"
    else:
        return "Непарне"

def main():
    try:
        age = int(input("Твій вік: "))
        result = check_age(age)
        print(f"Твій вік {result}.")
    except ValueError as i:
        print(f"Error: {i}")
    except Exception as o:
        print(f"Сталася неочікувана помилка: {0}")

if __name__ == "__main__":
    main()
#2
def day_of_week(number):
    if number == 1:
        return "Понеділок"
    elif number == 2:
        return "Вівторок"
    elif number == 3:
        return "Середа"
    elif number == 4:
        return "Четвер"
    elif number == 5:
        return "П'ятниця"
    elif number == 6:
        return "Субота"
    elif number == 7:
        return "Неділя"
    else:
        return "Такого дня у неділі немає!"

def main():
    try:
        number = int(input("Введи число (1-7), щоб отримати відповідний день тижня: "))
        if 1 <= number <= 7:
            day = get_day_of_week(number)
            print(f"Обранний день тижня це {day}.")
        else:
            print("Помилка. Вводіть число від 1 до 7.")
    except ValueError:
        print("Вводити можна лише число.")

if __name__ == "__main__":
    main()