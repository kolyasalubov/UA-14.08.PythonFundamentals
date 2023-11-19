import random
from tkinter import *
from pygame import mixer

mixer.init()
window = Tk()

window.geometry('1000x500')
window.resizable(width=False, height=False)
window.title('MAGIC EIGHT')
window.config(bg='white')
icon = PhotoImage(file='Logo 8.png')
window.iconphoto(True, icon)


def get_response():
    mixer.music.load("Mouse_Click.mp3")
    mixer.music.play()
    button.config(state="disabled")
    bool_list = [True, False]
    bool_value = random.choice(bool_list)
    if bool_value == 0:
        responses = ["There is,\nFOR YOU,\nSTRANGER", "NOPE", "CORRECT",
                     "Bad Idea", "Reply hazy,\nTRY AGAIN\nLATER",
                     "Can't\nREALLY SAY", "Take it\nTO THE\nBANK"]
        number = random.randint(1, len(responses))
        action = 8 - number - 1
        match action:
            case 0:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 1:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 2:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 3:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 4:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 5:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 6:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)

    elif bool_value == 1:
        responses = ["That's\nFOR YOU\nTO DECIDE", "Yep", "You bet", "A\nMEETING\nIS POSSIBLE",
                     "You're\nTHE DRIVER", "Yes,\nBUT NOT\nTONIGHT", "Most\nASSUREDLY",
                     "What\nDO YOU\nTHINK", "Turn\nON THE\nMOBILE PHONE"]
        number = random.randint(1, len(responses))
        action = 10 - number - 1
        match action:
            case 0:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 1:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 2:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 3:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 4:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 5:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 6:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 7:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)
            case 8:
                bool_list = [True, False]
                bool_value = random.choice(bool_list)
                if bool_value:
                    label.config(image=photo_2)
                    label.config(text=responses[action])
                    window.after(2000, clear_response)
                else:
                    label.config(image=photo_2)
                    label.config(text=random.choice(responses))
                    window.after(2000, clear_response)


def clear_response():
    label.config(text="")
    label.config(image=photo_1)
    button.config(state="active")


photo_1 = PhotoImage(file='1_Magic_eight.png')
photo_2 = PhotoImage(file='2_Magic_eight.png')
label = Label(window, text="", font=('Tahoma', 11),
              fg='sky blue', bg='#f5b942',
              relief='ridge', bd=4,
              image=photo_1, compound='center')
label.pack(side=RIGHT, anchor=S)

logo = PhotoImage(file='Eight.png')
button = Button(window, command=get_response,
                bg='black', relief='ridge', bd=4, activebackground='black',
                state=ACTIVE, image=logo, width='499', height='499')
button.pack(side=LEFT, anchor=S)

window.mainloop()
