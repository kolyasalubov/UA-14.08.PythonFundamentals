input_value = int(input("Enter the factorial number : "))

counter = 1
result = 1
a=[]
text=""

while True:

    if counter <= input_value:
        result *= counter
        text+=str(counter)
        if counter<input_value:
            text+="*"
    else:
        break
    counter += 1


print(f"The result : {input_value}!={text}={result}")
