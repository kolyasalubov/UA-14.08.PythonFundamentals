import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    location = entry_field.get()
    try:
        observation = mgr.weather_at_place(location)
        w = observation.weather

        status_label.config(text="Status: " + w.detailed_status)
        wind_label.config(text="Wind: {} m/s".format(w.wind()['speed']))
        humidity_label.config(text="Humidity: {}%".format(w.humidity))
        temperature_label.config(text="Temperature: {}°C".format(w.temperature('celsius')['temp']))
        clouds_label.config(text="Clouds: {}%".format(w.clouds))

    except Exception as e:
        status_label.config(text="Error: " + str(e))

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

status_label = tk.Label(lower_frame, font=('Courier', 14))
status_label.place(relx=0, rely=0, relwidth=1, relheight=0.2)

wind_label = tk.Label(lower_frame, font=('Courier', 14))
wind_label.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

humidity_label = tk.Label(lower_frame, font=('Courier', 14))
humidity_label.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

temperature_label = tk.Label(lower_frame, font=('Courier', 14))
temperature_label.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)

clouds_label = tk.Label(lower_frame, font=('Courier', 14))
clouds_label.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

root.mainloop()