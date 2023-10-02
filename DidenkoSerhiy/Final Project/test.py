import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Translator")
win.geometry("200x70")

def translation():
  word = entry.get()
  translator = Translator(service_urls=["translate.google.com"])
  translation = translator.translate(word,dest= "fr")
  lable1 = tk.Label(win, text=f'Translated word : {translation.text}',bg="yellow")
  lable1.grid(row=2,column=0)


label = tk.Label(win,text="Enter Word: ")
label.grid(row=0,column=0,sticky="W")

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button = tk.Button(win,text="Translate",command=translation)
button.grid(row=1,column=1)

win.mainloop()
  