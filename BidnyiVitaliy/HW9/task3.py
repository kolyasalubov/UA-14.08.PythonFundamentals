import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

def get_weather():
    observation = mgr.weather_at_place(city.get())
    w = observation.weather
    temp.set(str(w.temperature('celsius')['temp']))


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

city = tk.StringVar()
entry_field = tk.Entry(frame,textvariable = city, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label1 = tk.Label(lower_frame,text ='temperature', font=('Courier', 14))
label1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

temp = tk.StringVar()
label2 = tk.Label(lower_frame,textvariable = temp, font=('Courier', 14))
label2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)



root.mainloop()

