import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt

def calculate_bmi():
    try:
        wt = float(wt_entry.get())
        ht = float(ht_entry.get())
        
        if wt <= 0 or ht <= 0:
            messagebox.showerror("Error", "Please enter valid wt and ht values.")
            return
        
        bmi = wt / (ht ** 2)
        bmi_result_label.config(text="Your BMI: {:.2f}".format(bmi))
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        category_label.config(text="Category: " + category)
        
        # Saving data
        with open("bmi_data.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Date: {timestamp}, Weight: {wt} kg, ht: {ht} m, BMI: {bmi}, Category: {category}\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and ht.")
#creating histogram of the stored data with matplotlib library of python
def visualize_bmi_data():
    categories = {"Underweight": 0, "Normal": 0, "Overweight": 0, "Obese": 0}
    
    with open("bmi_data.txt", "r") as file:
        for line in file:
            if "Category:" in line:
                category = line.split("Category:")[1].strip()
                categories[category] += 1
    
    labels = list(categories.keys())
    values = list(categories.values())
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
    plt.title('BMI Categories Over Time')
    plt.xlabel('BMI Category')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def on_visualize_click():
    visualize_bmi_data()

root = tk.Tk()
root.title("BMI Calculator")

style = ttk.Style()
style.theme_use('clam')
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
wt_label = ttk.Label(frame, text="Enter your wt (kg):", font=("Arial Bold", 11))
wt_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
wt_entry = ttk.Entry(frame)
wt_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)
ht_label = ttk.Label(frame, text="Enter your ht (m):", font=("Arial Bold", 11))
ht_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
ht_entry = ttk.Entry(frame)
ht_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)
calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi, bg="#4caf50", fg="white", font=("Arial Bold", 12))
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)
visualize_button = tk.Button(frame, text="Visualize", command=on_visualize_click, bg="#2196f3", fg="white", font=("Arial Bold", 12))
visualize_button.grid(row=3, columnspan=2, padx=10, pady=10)
bmi_result_label = ttk.Label(frame, text="", font=("Arial Bold", 11))
bmi_result_label.grid(row=4, columnspan=2)
category_label = ttk.Label(frame, text="", font=("Arial Bold", 11))
category_label.grid(row=5, columnspan=2)
root.mainloop()
