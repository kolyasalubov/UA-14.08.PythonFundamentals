#First task: In the range from 1 to 10 determine even, odd and numbers aren't divisible by 2 and 3
print(list(range(1,11)))
Even_Numbers=[]
Odd_Numbers=[]
Other_Numbers=[]
for num in range(1,11):
    if num %2==0:
       Even_Numbers.append(num)
    elif num %2!=0 and num %3!=0:
        Odd_Numbers.append(num)
    elif num %3==0:
        Other_Numbers.append(num) 
print("Even numbers:",Even_Numbers)
print("Odd numbers:",Odd_Numbers)
print("Other numbers:",Other_Numbers)
print("-------------------------")

#Secont task: Write a script that checks the login that the user enters.
login = 'First' 
user_login = "" 
while user_login != login: 
  user_login = input('Please, enter you login:') 
  if user_login == login : 
    print('Welcome,',user_login) 
  else: 
    print('Error, Please try again')