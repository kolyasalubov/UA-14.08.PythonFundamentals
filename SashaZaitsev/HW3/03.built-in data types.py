# built-in data types
better = 0
never = 0
iss = 0

line_zen_python = input('Введіть рядок з "Zen of Python":').lower()
for i in line_zen_python.split():
    if i == 'better':
        better += 1
    elif i == 'never':
        never += 1
    elif i == 'is':
        iss += 1     
    else:
        pass

print(f'Всього "better" в рядку: {better}\nВсього "never" в рядку: {never}\nВсього "is" в рядку: {iss}')

line_zen_upper = line_zen_python.upper()
print(f'Рядок в Uppercase: {line_zen_upper}')
replase = line_zen_python.replace('i', '&')
print(f'Рядок із заміною літери "i": {replase}')



num = int(input("Введіть чотрицифрове натуральне число: "))

summ = sum(map(int, str(num)))
print(summ)


name = "Sasha"
pasword = "secret"
print(f'Змінні до:\n {pasword}, {name}')

name, pasword = pasword, name

print(f'Змінні після:\n {pasword}, {name}')