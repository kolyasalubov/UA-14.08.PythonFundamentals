# Программа, що перетворює список з класу int на float
numbers = [1, 2 , 3, 4, 5]
print("Перетворюємо числа у тип float")

for i in numbers:
    i = float(i)
    print(i)

# Програма виводе ряд Фібоначі до числа n
f1 = 1
f2 = 1

n = int(input("Введіть число до ряду Фібоначчі: "))

while n > 2:
    f1, f2 = f2, f1 + f2
    print(f2)
    n -= 1

# Программа виводе факторіал числа х
x = int(input("Введіть число, факторіал якого хочете знайти: "))
f = 1

for i in range(2, x + 1):
    f *= i
print(f"{x}! = {f}")