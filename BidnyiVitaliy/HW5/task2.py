# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

username = ""

while username!='First':
    
    username = input("Enter username: ")

    if username == 'First':
        print('Access is allowed.')
        break

    else:
        print('Access denied. Try again.')