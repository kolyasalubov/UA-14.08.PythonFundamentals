def fibonacci_sequence(n):
    fib_list = []
    a, b = 0, 1
    

    while a <= n:
        fib_list.append(a)
        a, b = b, a + b
        
    return fib_list
    
n = int(input("Input your number:"))
fibonacci_list = fibonacci_sequence(n)
print("Fibonacci list up to", n, ":", fibonacci_list)