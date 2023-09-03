#Print Fibonacci numbers up to the entered number n,
#using cycles.
#(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

fib1 = 1
fib2 = 1
 
n = int (input("Fibonacci series element number: "))
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print("The value of this element:", fib2)