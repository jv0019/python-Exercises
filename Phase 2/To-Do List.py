import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_completed():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(tk.END, task + " ✔")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as complete.")

def save_tasks():
    tasks = task_listbox.get(0, task_listbox.size())
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for task in f.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width=50, height=10, bd=0)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_task_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT)

mark_completed_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed)
mark_completed_button.pack(side=tk.LEFT)

save_tasks_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_tasks_button.pack(side=tk.LEFT)

load_tasks()

root.mainloop()
