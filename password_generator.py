
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        password_result.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def clear_fields():
    length_entry.delete(0, tk.END)
    password_result.set("")
    letters_var.set(0)
    numbers_var.set(0)
    symbols_var.set(0)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_result.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x420")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Password Length:", font=("Arial", 11)).pack()
length_entry = tk.Entry(root, font=("Arial", 11))
length_entry.pack(pady=5)

# Options
letters_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Copy Password", command=copy_password).pack()
tk.Button(root, text="Clear", command=clear_fields, bg="#f44336", fg="white").pack(pady=5)

# Result
password_result = tk.StringVar()
tk.Entry(root, textvariable=password_result, font=("Arial", 12), justify="center").pack(pady=10)

root.mainloop()
