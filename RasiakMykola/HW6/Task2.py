
# 06.1 PRACTICAL TASKS / [GITHUB]

# Task_2
login_user = list(input('\nPlease enter your login: '))
checking_login = {0: 70, 1: 105, 2: 114, 3: 115, 4: 116}

i = 0
while i < len(login_user):
    login_user.append(ord(login_user.pop(0)))
    if login_user:
        dic_login = dict(enumerate(login_user))
        
    i = i + 1
    

print('Welcome, First') if(dic_login == checking_login) else print('Sorry, you have entered an incorrect login')




