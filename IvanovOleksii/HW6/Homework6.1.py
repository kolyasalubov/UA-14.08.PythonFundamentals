resoult_even = []
resoult_odd = []
resoult_remainder = []
for i in range(1, 10):
    if i % 2 == 0:
        resoult_even.append(i)
    elif i % 3 == 0:
        resoult_odd.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        resoult_remainder.append(i)

print(f'Even number that are divisble by 2: {resoult_even}')
print(f'Odd number that are divisble by 3: {resoult_odd}')
print(f'Numbers that are not divisble by 2 or 3: {resoult_remainder}')


