
import tkinter as tk
from tkinter import messagebox, filedialog
import os

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        del tasks[index]
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def edit_task():
    try:
        index = task_listbox.curselection()[0]
        new_task = task_entry.get().strip()
        if new_task:
            tasks[index] = new_task
            update_listbox()
            task_entry.delete(0, tk.END)
            save_tasks()
        else:
            messagebox.showwarning("Input Error", "Enter a new value for the task.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

def mark_completed():
    try:
        index = task_listbox.curselection()[0]
        task = tasks[index]
        if not task.startswith("✔️"):
            tasks[index] = "✔️ " + task
            update_listbox()
            save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task.")

def search_task():
    query = task_entry.get().strip().lower()
    if query:
        filtered = [task for task in tasks if query in task.lower()]
        update_listbox(filtered)
        if not filtered:
            messagebox.showinfo("Search Result", "No matching tasks found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

def reset_list():
    update_listbox()

def filter_tasks(filter_type):
    if filter_type == "All":
        update_listbox()
    elif filter_type == "Completed":
        update_listbox([t for t in tasks if t.startswith("✔️")])
    elif filter_type == "Pending":
        update_listbox([t for t in tasks if not t.startswith("✔️")])

# Task Management 

def update_listbox(display_list=None):
    task_listbox.delete(0, tk.END)
    for task in (display_list if display_list is not None else tasks):
        task_listbox.insert(tk.END, task)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
        update_listbox()



root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="white")
root.resizable(False, False)

tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="white", fg="#4a4a4a").pack(pady=10)


input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=5)

task_entry = tk.Entry(input_frame, font=("Arial", 14), width=25, bd=2, relief="groove")
task_entry.pack(side=tk.LEFT, padx=10)

tk.Button(input_frame, text="Add", command=add_task, bg="#4caf50", fg="white",
          font=("Arial", 12, "bold"), padx=10).pack(side=tk.LEFT)


task_listbox = tk.Listbox(root, width=45, height=12, font=("Arial", 14), bd=2, relief="sunken",
                          selectbackground="#4caf50", selectforeground="white")
task_listbox.pack(pady=15)


action_frame = tk.Frame(root, bg="white")
action_frame.pack(pady=5)

btn_style = {"font": ("Arial", 12, "bold"), "bg": "#3CB371", "fg": "white", "padx": 8, "pady": 4}

tk.Button(action_frame, text="Delete", command=delete_task, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(action_frame, text="Edit", command=edit_task, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(action_frame, text="Complete", command=mark_completed, **btn_style).grid(row=0, column=2, padx=5)


search_frame = tk.Frame(root, bg="white")
search_frame.pack(pady=10)

tk.Button(search_frame, text="Search", command=search_task, bg="#1E90FF", fg="white",
          font=("Arial", 12, "bold"), padx=10).pack(side=tk.LEFT, padx=5)

tk.Button(search_frame, text="Show All", command=reset_list, bg="#999999", fg="white",
          font=("Arial", 12, "bold"), padx=10).pack(side=tk.LEFT, padx=5)


filter_frame = tk.Frame(root, bg="white")
filter_frame.pack(pady=5)

tk.Label(filter_frame, text="View:", bg="white", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(filter_frame, text="All", command=lambda: filter_tasks("All"), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(filter_frame, text="Pending", command=lambda: filter_tasks("Pending"), **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(filter_frame, text="Completed", command=lambda: filter_tasks("Completed"), **btn_style).pack(side=tk.LEFT, padx=5)


load_tasks()


root.mainloop()
