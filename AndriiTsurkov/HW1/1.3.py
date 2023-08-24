from pyowm import OWM
import tkinter as tk
#from tkinter import font

# ---------- FREE API KEY examples ---------------------

API_KEY = '067cbd7c69671d70bd144b732a91c995'
HEIGHT = 350
WIDTH = 450


#input_city = 'lviv'
def  weather_response(input_city, API_KEY):

    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        #input_city = input("In which city are you interested in the weather?:")
        #input_city = 'Kiev'

        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(input_city)
        w = observation.weather

        # w.detailed_status         # 'clouds'
        # w.wind()                  # {'speed': 4.6, 'deg': 330}
        # w.humidity                # 87
        # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        # w.rain                    # {}
        # w.heat_index              # None
        # w.clouds                  # 75


        weather_result = (f"City: {input_city}\nConditions: {w.detailed_status }\nTemperature is {round(w.temperature('celsius')['temp'], 2)} C")
        weather_result += (f"\nWind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}")
        return weather_result

    except:
        return 'Oops! There was a problem\nretrieving that information.'


def get_weather(input_city, API_KEY):
    label['text'] = weather_response(input_city, API_KEY)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

### entry place
entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

### out place
button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get(), API_KEY))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()