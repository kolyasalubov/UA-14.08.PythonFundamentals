import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    # Search for current weather in your city and get details
    your_city = entry_field.get()
    observation = mgr.weather_at_place(your_city)
    w = observation.weather

    status = w.detailed_status
    wind = w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')
    rain = w.rain
    clouds = w.clouds
    get_weather_your_city = f"'Status' = {status}\n" \
                            f"'Wind' = {wind['speed']} mph\n" \
                            f"'Humidity' = {humidity}%\n" \
                            f"'Temperature' = {temperature['temp']}°C\n" \
                            f"'Rain' = {rain}\n" \
                            f"'Clouds' = {clouds}%"

    label.config(text=get_weather_your_city)


HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier New', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier New', 9),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier New', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()