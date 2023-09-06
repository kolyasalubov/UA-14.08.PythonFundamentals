input_value = int(input("Enter the value of the last number you want to have in Fibonacci list : "))

fibonacci_list = [0, 1]

counter = 1

while True:
    sum_numbers = fibonacci_list[counter] + fibonacci_list[counter - 1]
    if sum_numbers <= input_value:
        fibonacci_list.append(sum_numbers)
    else:
        break
    counter += 1


print(fibonacci_list)
