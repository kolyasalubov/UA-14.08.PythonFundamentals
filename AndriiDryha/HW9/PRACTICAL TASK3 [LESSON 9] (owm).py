
from pyowm import OWM
import tkinter as tk
from tkinter import font

# ---------- FREE API KEY examples ---------------------

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450



def weather_response():

    owm = OWM('ef2206ff5da67de63306d0b143e20872')
    mgr = owm.weather_manager()

    

    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87   
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75
    
    # status_clouds = w.detailed_status        # 'clouds'
    speed_wind = w.wind()['speed']                  # {'speed': 4.6, 'deg': 330}
    humidity = w.humidity                # 87   
    temperature_max = w.temperature('celsius')['temp_max']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    temperature = w.temperature('celsius')['temp']
    temperature_min = w.temperature('celsius')['temp_min']
    rain = w.rain                    # {}
    clouds = w.clouds                # 75

    # print(f"In {entry_field.get()} the wind speed is {speed_wind} km/hours")
    # print(f"In {entry_field.get()} the humidity of the air is {humidity} %")
    # print(f"In {entry_field.get()} the temperature of the air is {temperature} °C")
    # print(f"In {entry_field.get()} the maximum temperature of the air is {temperature_max} °C")
    # print(f"In {entry_field.get()} the minimum temperature of the air is {temperature_min} °C")
    # print(f"In {entry_field.get()} the cloudy is {clouds} %")
    # print(f"In {entry_field.get()} the precipitation is {rain}")

    return f"""The wind speed is {speed_wind} km/hours 
    The humidity of the air is {humidity} % 
    The temperature of the air is {temperature} °C 
    The maximum temperature of the air is {temperature_max} °C 
    The minimum temperature of the air is {temperature_min} °C 
    The cloudy is {clouds} %"""




def get_weather():
      
    label['text'] = weather_response()










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
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame,
                 text=[],
                 bg="white",
                 font=('Courier', 8))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()