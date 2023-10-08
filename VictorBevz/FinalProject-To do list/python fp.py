import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

def add_task():
    task = entry.get()
    due_date = due_date_entry.get()
    if task and due_date:
        task_with_due_date = f"{task} (Due: {due_date})"
        listbox.insert(tk.END, task_with_due_date)
        entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task and due date!")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Advanced To-Do List")

entry = tk.Entry(root, width=30)
due_date_label = tk.Label(root, text="Due Date (DD-MM-YYYY):")
due_date_entry = tk.Entry(root, width=15)
entry.pack(pady=10)
due_date_label.pack()
due_date_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
load_button = tk.Button(root, text="Load Tasks", command=load_tasks)

add_button.pack()
remove_button.pack()
clear_button.pack()
save_button.pack()
load_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

load_tasks()

root.mainloop()
