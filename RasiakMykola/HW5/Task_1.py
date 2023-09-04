
# 05.1 PRACTICAL TASKS / [GITHUB]

#Task1
user_number = list(range(1, 1+int(input('\nEnter an positive integer to create a list of elements of type \'float\': '))))

if len(user_number) == 0:
     print('Please try again')
else:
    for i in user_number:
        float_number = user_number.pop(0)
        user_number.append(float(float_number))
        
    print("Print floating-point numbers in a list:")
    print(f'{user_number}')


  


    
  
