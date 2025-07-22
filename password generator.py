import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = password_length.get()
    if not length.isdigit() or int(length) < 4:
        messagebox.showerror("Invalid Input", "Please enter a number (minimum 4).")
        return

    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(padx=20, pady=20)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack()
password_length = tk.Entry(root, font=("Arial", 12), justify='center')
password_length.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify='center')
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#2196F3", fg="white", command=copy_password).pack(pady=10)

root.mainloop()
