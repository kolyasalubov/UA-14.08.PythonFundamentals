#9.3 
from pyowm import OWM
import tkinter as tk
from tkinter import font



API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------




def get_weather():
    entered_city = entry_field.get()
    observation = mgr.weather_at_place(entered_city)
    w = observation.weather

    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)                  # 75

HEIGHT = 350
WIDTH = 450
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

owm = OWM(API_KEY)
mgr = owm.weather_manager()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()


