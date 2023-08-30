input_nymber = int(input("Enter the number of Fibonacci terms to generate: "))
num1, num2 = 0, 1
fibo_sequence = [num1, num2]

while len(fibo_sequence) < input_nymber:
    num3 = num1 + num2
    fibo_sequence.append(num3)
    num1, num2 = num2, num3
    
print(fibo_sequence)