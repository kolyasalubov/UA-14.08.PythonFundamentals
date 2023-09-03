final_number = int(input('Enter the final number: '))

num1 = 0
num2 = 1
resoult = 0
print(f'{num1}\n'
      f'{num2}')

while True:
    if resoult < final_number:
        resoult = num1 + num2
        num1 = num2
        num2 = resoult
        print(resoult)
    else:
        break
