for n in range(1, 10):
    if n % 2 == 0:
        print('{} is even number'.format(n))
    if    (n%2 == 1) and(n%3 == 0):
        print('{} is odd number, which is divisible by 3'.format(n))
    if    (n%2 != 0) and(n%3 != 0):
        print('{} is not divisible by 2 and 3'.format(n))