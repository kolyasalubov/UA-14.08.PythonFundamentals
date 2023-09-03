item_value = int(input("Enter your number: "))

fibonachi_list = [0, 1]

while fibonachi_list[-1] < item_value:
    fibonachi_list.append(fibonachi_list[-2] + fibonachi_list[-1])

fibonachi_list.pop()
print(f'Your number {item_value}. Fibonacci list for your number:\n{fibonachi_list}')
