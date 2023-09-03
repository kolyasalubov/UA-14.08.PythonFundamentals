#First task: Create a list
num_list=int(input("Enter amount of list:"))
List=[0]
while len(List)<=num_list:
      List.append(float(List[-1]+1))
print(List)

print("-----------------------------")

#Second task: Print Fibonacci numbers
n_num=int(input('Enter last n: '))
fib=[0,1]
while len(fib)<=n_num:
    fib.append(fib[-2]+fib[-1])
print(fib)

print("--------------------------")

#Third task: calculate the factorial
n_fact = int(input("Enter numeric:"))
factor = 1
for i in range(2, n_fact+1):
    factor *= i
print(factor)

