login = 'First' 
user_login = "" 
while user_login != login: 
  user_login = input('Please, enter you login:') 
  if user_login == login : 
    print('Welcome,',user_login) 
  else: 
    print('Error, Please try again')