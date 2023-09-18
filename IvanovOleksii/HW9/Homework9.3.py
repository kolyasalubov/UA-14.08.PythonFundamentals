import tkinter as tk
from tkinter import font
from pyowm import OWM


def get_weather():
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    clouds = w.detailed_status  # 'clouds'
    wind = w.wind()['speed']  # {'speed': 4.6, 'deg': 330}
    humidity = w.humidity  # 87
    temp_max = (w.temperature('celsius')['temp_max'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    temp = (w.temperature('celsius')['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    temp_min = (w.temperature('celsius')['temp_min'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain = w.rain  # {}
    cloud_index = w.clouds  # 75

    res = (f'clouds: {clouds}, {cloud_index}\n'
           f'wind: {wind}\n'
           f'humidity: {humidity}\n'
           f'temp max: {temp_max}\n'
           f'temp: {temp}\n'
           f'temp min: {temp_min}\n'
           f'rain: {rain}')
    return res


def label_weather():
    label['text'] = get_weather()


def main():
    get_weather()


HEIGHT = 350
WIDTH = 450

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
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: label_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

if __name__ == '__main__':
    main()
