from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import datetime
import os

root = Tk()  # створюєм корневий об'єкт - вікно

#root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))     # встановлюємо розміри вікна
root.title("CAT")                       # встановлюємо заголовок вікна


icon = PhotoImage(file="./images/iconCat.png")       # альтернативна опція встановлення іконки
#icon = PhotoImage(file="D:/pythone/git_hub/UA-14.08.PythonFundamentals/AndriiTsurkov/TCP/images/iconCat.png")
root.iconphoto(False, icon)                         # альтернативна опція встановлення іконки

cats_pictures = PhotoImage(file="./images/2.png")   # створюємо об'єкт зображення
logo = Label(root, image=cats_pictures)             # створюємо об'єкт зображення https://www.pythontutorial.net/tkinter/tkinter-photoimage/

game = 3                                # умова продовження гри
healthCat = 20                          # "здоров'я,"
leisureCat = 20                         # leisure - "задоволення"
speed_cat_condition_decreases = 3       # швидкість зменшення стану кота"

menu_flag = False                       # True False, щоб увімкнути гру, після закриття меню

start_time = datetime.datetime.now()    # Час початку гри
time_in_game = ""                       # як довго ти в грі
def update_clock():
    global menu_flag
    global start_time
    global time_in_game

    ''' функція, яка відповідає за оновлення ігрової ситуації раз на секунду '''
    root.after(1000, update_clock)
    root.after(1000, heppimin)

    time_now = datetime.datetime.now()  # оновлення времені
    time_in_game = time_now - start_time 
    time_in_game = str(time_in_game)
    time_in_game = time_in_game.split(":")
    seconds = time_in_game[2]
    seconds = seconds[:2]
    time_in_game = f"{time_in_game[0]}:{time_in_game[1]}:{seconds}"
    time_label.configure(text="Time in game: " + time_in_game)

    change_cats_pictures()          # зміна картинки кота

def heppimin():
    global healthCat                # працюємо з глобальними аргументами
    global leisureCat               # працюємо з глобальними аргументами
    
    global menu_flag
    global speed_cat_condition_decreases
    global game
    
    if healthCat <= 0 or leisureCat <= 0:
        if not menu_flag:
            menu_flag = True        # Flag
            answer = mb.askyesno(title="You lost", message="Do you want to play again?")
            if answer == True:      # Flag
                healthCat += 50
                leisureCat += 50
                menu_flag = False   # Flag
            else:
                game = 1
                exit()
    elif healthCat >= 100 and leisureCat >= 100:
        if not menu_flag:           # Flag
            menu_flag = True        # Flag
            answer2 = mb.askyesno(title="You win", message="Do you want to play again?")
            if answer2 == True:
                healthCat -= 50
                leisureCat -= 50
                menu_flag = False   # Flag
            else:
                game = game + 1
                exit()
    

    if not menu_flag:               # Flag
        if healthCat >= 0:
            if healthCat - speed_cat_condition_decreases < 0:
                healthCat = 0
            else:
                healthCat = healthCat - speed_cat_condition_decreases       # кожної ітерації параметр "здоров'я," зменшується на 3

        if leisureCat >= 0:
            if leisureCat - speed_cat_condition_decreases < 0:
                leisureCat = 0                       
            else:
                leisureCat = leisureCat - speed_cat_condition_decreases     # кожної ітерації параметр "задоволення" зменшується на 3

        l1.configure(text="health - " + str(healthCat) + "%")               # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")             # змінюємо налаштування текстової мітки "задоволення"

def health():
    global healthCat
    global leisureCat
    healthCat = healthCat + 10
    leisureCat = leisureCat - 2
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is healh")
    if leisureCat <= 10:
        mb.showerror("sorry", "your cat is sad")
        leisureCat = leisureCat + 20

def leisure():
    global healthCat
    global leisureCat
    healthCat = healthCat - 2
    leisureCat = leisureCat + 10
    l1.configure(text="health - " + str(healthCat) + "%")
    l2.configure(text="leisure - " + str(leisureCat) + "%")
    l3.configure(text="your cat is laisure")
    if healthCat <= 10:
        mb.showerror("sorry", "your cat is ill")
        healthCat = healthCat + 20

def change_cats_pictures():
    '''Функція зміни картинок кота '''
    global healthCat
    global leisureCat

    logo1 = PhotoImage(file="./images/2.png")      # NORMAL pictures
    logo2 = PhotoImage(file="./images/1.png")      # ILL pictures
    logo3 = PhotoImage(file="./images/3.png")      # WIN pictures
    logo4 = PhotoImage(file="./images/4.png")      # DEAD pictures

    if healthCat <= 20 or leisureCat <= 20:
        logo.configure(image=logo2)
        logo.image = logo2

    if healthCat > 21 and leisureCat > 21:
        logo.configure(image=logo1)
        logo.image = logo1
    
    if healthCat >= 80 and leisureCat >= 80:
        logo.configure(image=logo3)
        logo.image = logo3
   
    if healthCat == 0 or leisureCat == 0:
        logo.configure(image=logo4)
        logo.image = logo4

while game == 3:

    label2 = Label(width=27, height=3, text="It is your Cat", font="Arial")
    time_label = Label(width=27, height=2, text="Time in game:" + time_in_game, font=("Arial", 9))
    b1 = ttk.Button(width=15, text="feed", command=health)      # годувати
    b2 = ttk.Button(width=15, text="caress", command=leisure)   # пестити
    b3 = ttk.Button(width=15, text="train", command=health)     # виховувати, тренувати
    b4 = ttk.Button(width=15, text="play", command=leisure)     # грати
    b5 = ttk.Button(width=15, text="Exit", command=quit)        # вихід
    l1 = Label(width=20, height=3, text="health - " + str(healthCat) + "%")     # здоров'я,
    l2 = Label(width=20, height=2, text="leisure - " + str(leisureCat) + "%")   # задоволення, дозвілля
    l3 = Label(width=20, height=2, text="your cat is alive")    # здоровий


    label2.grid(row=0, column=2, columnspan=3, rowspan=2)
    time_label.grid(row=0, column=0, columnspan=1, rowspan=3)    # видображення часу у грі
    b1.grid(row=2, column=0)
    b2.grid(row=3, column=0)
    b3.grid(row=4, column=0)
    b4.grid(row=5, column=0)
    b5.grid(row=9, column=3)
    l1.grid(row=6, column=0)
    l2.grid(row=7, column=0)
    l3.grid(row=7, column=3)
    logo.grid(row=2, column=2, columnspan=5, rowspan=5)         # pictures of cat

    update_clock()
    root.mainloop()  # Для відображення вікна та взаємодії з користувачем у вікна викликається метод mainloop()


