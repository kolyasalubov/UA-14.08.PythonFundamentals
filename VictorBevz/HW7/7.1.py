n1 = int(input("Select first number:"))
n2 = int(input("Select second number:"))

def largest_number(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        print("Numbers are equal")
        return (n1, n2) 

result = largest_number(n1, n2)
print("Larger number is:", result)
 