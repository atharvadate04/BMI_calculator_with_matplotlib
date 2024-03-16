import requests
import tkinter as tk
from tkinter import messagebox

def fetch_weather():
    location = location_entry.get()
    api_key = "" #Your Api Key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'message' in data:
            messagebox.showerror("Error", data['message'])
        else:
            temp = data['main']['temp']
            hum = data['main']['humidity']
            condition = data['weather'][0]['description'].capitalize()
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            
            weather_label.config(text=f"Temperature: {temp}°C\nHumidity: {hum}%\nWeather Condition: {condition}")
            icon_image = tk.PhotoImage(data=requests.get(icon_url).content)
            weather_icon.config(image=icon_image)
            weather_icon.image = icon_image 
            
            new_bg_color = "#FFD700" if temp > 27 else "#ADD8E6"
            root.configure(bg=new_bg_color) 
            title_label.configure(bg=new_bg_color)
            location_label.configure(bg=new_bg_color)
            weather_label.configure(bg=new_bg_color)
            weather_frame.configure(bg=new_bg_color)
            weather_icon.configure(bg=new_bg_color)
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.configure(bg="#F0F0F0")
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 20))
title_label.pack(pady=10)
location_label = tk.Label(root, text="Enter Location:", font=("Helvetica", 12))
location_label.pack()
location_entry = tk.Entry(root, width=30)
location_entry.pack()
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, bg="#90EE90", font=("Helvetica", 10, "bold"))
fetch_button.pack(pady=10)
weather_frame = tk.Frame(root)
weather_frame.pack(pady=20)
weather_label = tk.Label(weather_frame, text="", font=("Helvetica", 14))
weather_label.pack()
weather_icon = tk.Label(weather_frame)
weather_icon.pack()

root.mainloop()
