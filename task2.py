import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        window.title("Advanced Password Generator")
        window.configure(bg="#f0f0f0")
        window.geometry("400x300")
        self.label = tk.Label(window, text="Specify Password Length and Conditions:", bg="#f0f0f0", font=("Arial Bold", 11))
        self.label.pack()
        self.password_length = tk.Scale(window, from_=6, to=30, orient=tk.HORIZONTAL, bg="#f0f0f0")
        self.password_length.pack()
        self.upv = tk.IntVar()
        self.uc = tk.Checkbutton(window, text="Include Uppercase Letters", var=self.upv, bg="#f0f0f0", font=("Arial Bold", 10))
        self.uc.pack()
        self.lwv = tk.IntVar()
        self.lc = tk.Checkbutton(window, text="Include Lowercase Letters", var=self.lwv, bg="#f0f0f0", font=("Arial Bold", 10))
        self.lc.pack()
        self.digits_var = tk.IntVar()
        self.digits = tk.Checkbutton(window, text="Include Digits                    ", var=self.digits_var, bg="#f0f0f0", font=("Arial Bold", 10))
        self.digits.pack()
        self.spl_char = tk.IntVar()
        self.spl = tk.Checkbutton(window, text="Include Special Characters", var=self.spl_char, bg="#f0f0f0", font=("Arial Bold", 10))
        self.spl.pack()
        self.generate_button = tk.Button(window, text="Generate Password", command=self.generate_password, bg="#4caf50", fg="white", font=("Arial Bold", 12))
        self.generate_button.pack()
        self.label = tk.Label(window, text="", bg="#f0f0f0", font=("Arial Bold", 12))
        self.label.pack()
        self.copy_button = tk.Button(window, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#2196f3", fg="white", font=("Arial Bold", 12))
        self.copy_button.pack(pady=10)

    def generate_password(self):
        password_length = self.password_length.get()
        passwrd_chars = ''
        if self.upv.get():
            passwrd_chars += string.ascii_uppercase
        if self.lwv.get():
            passwrd_chars += string.ascii_lowercase
        if self.digits_var.get():
            passwrd_chars += string.digits
        if self.spl_char.get():
            passwrd_chars += string.punctuation
        if passwrd_chars == '':
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        password = ''.join(random.choice(passwrd_chars) for i in range(password_length))
        self.label.config(text="Generated Password: " + password)

    def copy_to_clipboard(self):
        password = self.label.cget("text").split(": ")[1]
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

root = tk.Tk()
my_password_generator = PasswordGenerator(root)
root.mainloop()