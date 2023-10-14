from tkinter import *
from tkinter import ttk #,messagebox
import googletrans
from googletrans import Translator
#import config

root = Tk()
root.title("Google translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background = "lightblue")
#key = config.api_key

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text = c)
    label2.configure(text = c1)
    root.after(1000,label_change) #time

def translate_now():
    text_ = text1.get(1.0,END)
    t1 = Translator(service_urls = ["translate.google.com"])
    trans_text = t1.translate(text_, src = combo1.get(), dest = combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)
    
#icon
image_icon = PhotoImage(file = "sticker.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file = "PIC.png")
image_label = Label(root, image = arrow_image, width = 300)
image_label.place(x = 400, y = 50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values = languageV, font = "Roboto 14", state = "r")
combo1.place(x = 110, y = 20)
combo1.set("English")

label1 = Label(root, text = "English", font = "segoe 30 ", bg = "white", width = 14,\
             bd = 5, relief = GROOVE, background = "lightyellow")
label1.place(x = 10, y = 50)


combo2 = ttk.Combobox(root, values = languageV, font = "Roboto 14", state = "r")
combo2.place(x = 720, y = 20)
combo2.set("Select Language")

label2 = Label(root, text = "ENGLISH", font = "segoe 30 ", bg = "white", width = 14, bd = 5,\
             relief = GROOVE, background = "lightyellow")
label2.place(x = 720, y = 50)

# 1st frame
f = Frame(root, bg = "Black", bd = 5)
f.place(x = 10, y = 118, width = 350, height = 210)

text1 = Text(f, font = "Roboto 20", bg = "white", relief = GROOVE, wrap = WORD)
text1.place(x = 0, y = 0, width = 350, height = 200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side = "right", fill = 'y')

scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)


# 2st frame
f2 = Frame(root, bg = "Black", bd = 5)
f2.place(x = 720, y = 118, width = 350, height = 210)

text2 = Text(f2, font = "Roboto 20", bg = "white", relief = GROOVE, wrap = WORD)
text2.place(x = 0, y = 0, width = 350, height = 200)

scrollbar2 = Scrollbar(f2)
scrollbar1.pack(side = "right", fill = 'y')

scrollbar2.configure(command = text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)

#translate button
translate = Button(root,text = "Translate", font = ("Roboto", 15), activebackground = "white",\
                 cursor = "hand2", bd = 1, width = 10, height = 2, bg = "black", fg = "white",\
                    command = translate_now)
translate.place(x = 476, y = 250)



label_change()
root.mainloop()
              
