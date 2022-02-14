import requests
import tkinter as tk
from tkinter import ttk


# construct URL to get weather info
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city = "toronto"
api_key = "1553041b927b19bb4b342ea44c09fda9" # https://home.openweathermap.org/api_keys
url = f'{base_url}q={city}&appid={api_key}'
print(url)

def get_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "1553041b927b19bb4b342ea44c09fda9"
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp.json()

def get_current_temp_in_c(city):
    data = get_weather_data(city)
    current_temp = data['main']['temp']
    current_temp_in_c = f'{round(current_temp - 273.15)} C'
    return current_temp_in_c

def get_condition(city):
    data = get_weather_data(city)
    current_condition = data['weather'][0]['description']
    return current_condition
def get_feels_like(city):
    data = get_weather_data(city)
    feels_like = data['main']['feels_like']
    feels_like_in_c = f"{round(feels_like - 273.15)} C"
    return feels_like_in_c
def get_wind_speed(city):
    data = get_weather_data(city)
    wind_speed = data['wind']['speed']
    wind_speed_ms = f'{wind_speed} m/s'
    return wind_speed_ms
def get_wind_gusts(city):
    data = get_weather_data(city)
    wind_gusts = data['wind']['gust']
    wind_gusts_ms = f'{wind_gusts} m/s'
    return wind_gusts_ms

def get_weather_action():
    get_weather_data(city_name.get())
    temp.set(f'{get_current_temp_in_c(city_name.get())}')
    wind_chill.set(f'{get_feels_like(city_name.get())}')
    condition.set(f'{get_condition(city_name.get())}')
    wind.set(f'{get_wind_speed(city_name.get())}')
    gusts.set(f'{get_wind_gusts(city_name.get())}')

# Create the root window
root = tk.Tk()
root.title('Sean\'s Weather App')
root.geometry('300x400')

# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


# Create a city label
ttk.Label(frame_home, text="enter city: ").grid(column=0, row=1)


# create city entry box
city_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=city_name).grid(column=1, row=1, padx=5, pady=5)


#creat get weather button
ttk.Button(frame_home, text='Get Weather Data', command=get_weather_action).grid(column=1, row=2, padx=5, pady=5)

# Create a temp label
ttk.Label(frame_home, text="Current Temp: ").grid(column=0, row=3)

#create temp entry box
temp = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=temp).grid(column=1, row=3, padx=5, pady=5)

# Create a wind chill label
ttk.Label(frame_home, text="Feel Like: ").grid(column=0, row=4)

#create wind chill entry box
wind_chill = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind_chill).grid(column=1, row=4, padx=5, pady=5)

# Create a summary label
ttk.Label(frame_home, text="summary: ").grid(column=0, row=5)
#create summary entry box
condition = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=condition).grid(column=1, row=5, padx=5, pady=5)

# Create a wind speed label
ttk.Label(frame_home, text="Wind Speed: ").grid(column=0, row=6)
#create wind speed entry box
wind = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=wind).grid(column=1, row=6, padx=5, pady=5)

# Create a wind gusts label
ttk.Label(frame_home, text="Wind Gusts: ").grid(column=0, row=7)

#create gust entry box
gusts = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=gusts).grid(column=1, row=7, padx=5, pady=5)








root.mainloop()