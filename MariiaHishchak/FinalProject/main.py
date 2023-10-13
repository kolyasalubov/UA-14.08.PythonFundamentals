import tkinter as tk
from tkinter import scrolledtext

class TransportRoute:
    def __init__(self, initial_station, final_station, number_of_stops, route_length_in_km):
        self.initial_station = initial_station
        self.final_station = final_station
        self.number_of_stops = number_of_stops
        self.route_length_in_km = route_length_in_km

    def display_info(self):
        return f"\n-Initial station: {self.initial_station} \nFinal station: {self.final_station} " \
               f"\nNumber of stops: {self.number_of_stops} \nRoute length in km: {self.route_length_in_km}"

with open('routes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

routes = []

for line in lines:
    data = line.strip().split(', ')
    if len(data) == 4:
        initial_station, final_station, number_of_stops, route_length_in_km = data
        route = TransportRoute(initial_station, final_station, int(number_of_stops), float(route_length_in_km))
        routes.append(route)

file.close()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transport Route")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self)
        self.text_area.pack(fill="both", expand=True)

        menu = tk.Menu(self)
        self.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        command_menu = tk.Menu(menu)
        menu.add_cascade(label="Commands", menu=command_menu)
        command_menu.add_command(label="Print all routes", command=self.print_all_routes)
        command_menu.add_command(label="Print sorted by length routes", command=self.print_sorted_by_length_routes)

        ############################################
        x_route_label = tk.Label(self, text="Enter X for average length:")
        x_route_label.pack()


        self.x_route_entry = tk.Entry(self)
        self.x_route_entry.pack()


        filter_button = tk.Button(self, text="Filter Routes", command=self.print_routes_less_than_x)
        filter_button.pack()

        ############################################
        x_station_label = tk.Label(self, text="Enter initial station X:")
        x_station_label.pack()


        self.x_station_entry = tk.Entry(self)
        self.x_station_entry.pack()


        filter_station_button = tk.Button(self, text="Filter Routes by Station",
                                          command=self.print_routes_starting_with_x)
        filter_station_button.pack()

        ###########################################
        clear_button = tk.Button(self, text="Clear", command=self.clear)
        clear_button.pack()

    def print_all_routes(self):
        self.text_area.delete('1.0', tk.END)
        for route in routes:
            info = route.display_info()
            self.text_area.insert(tk.END, info + "\n")

    def print_sorted_by_length_routes(self):
        self.text_area.delete('1.0', tk.END)
        sorted_routes = sorted(routes, key=lambda y: y.route_length_in_km)
        for route in sorted_routes:
            info = route.display_info()
            self.text_area.insert(tk.END, info + "\n")

    def print_routes_less_than_x(self):
        x_route_str = self.x_route_entry.get()

        try:
            x_route = float(x_route_str)
        except ValueError:

            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, "Invalid input for X. Please enter a valid number.")
            return

        self.text_area.delete('1.0', tk.END)

        def average_length_less_than_x(route, x_route):
            return route.route_length_in_km / route.number_of_stops < x_route

        filtered_routes = filter(lambda route: average_length_less_than_x(route, x_route), routes)
        count = len(list(filtered_routes))

        result_text = f"Number of routes with average length less than {x_route}: {count}"
        self.text_area.insert(tk.END, result_text)

    def print_routes_starting_with_x(self):
        x_station = self.x_station_entry.get()

        self.text_area.delete('1.0', tk.END)

        routes_starting_with_x = [route for route in routes if route.initial_station == x_station]

        if not routes_starting_with_x:
            self.text_area.insert(tk.END, f"No routes found starting at station {x_station}.")
            return

        for route in routes_starting_with_x:
            info = route.display_info()
            self.text_area.insert(tk.END, info + "\n\n")

    def clear(self):
        self.text_area.delete('1.0', tk.END)
        self.x_route_entry.delete(0, tk.END)
        self.x_station_entry.delete(0, tk.END)

app = Application()
app.mainloop()
