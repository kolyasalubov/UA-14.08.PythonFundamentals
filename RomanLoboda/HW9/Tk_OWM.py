import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450


def get_weather():
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    weather_detail = f"Status: {w.detailed_status}\n"
    weather_detail += f"Temperature:{w.temperature('celsius')['temp']}°C\n"
    weather_detail += f"Wins: {w.wind()['speed']} m/s\n"
    weather_detail += f"Humidity: {w.humidity}%\n"
    label.config(text=weather_detail)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="black", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

print(label)

root.mainloop()
