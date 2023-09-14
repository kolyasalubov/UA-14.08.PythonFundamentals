#2 login

while True:

    print("For exit enter 'q'.")
    login_name = input('Please enter your login name: ')
    #print (len(login_name))

    if len(login_name) == 0:
        print("Error: You didn't enter anything. Please try again.\n")
    elif login_name == "First":
        print("Hello First! We hava a glad to see you again.\n")
    elif login_name == "q":
        print("Thank you for your visit.\n")
        break
    else:
        print("We don't have such login in our system.\n")