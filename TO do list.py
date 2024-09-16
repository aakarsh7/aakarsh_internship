import tkinter as tk
from tkinter import messagebox

# Functions for the To-Do app
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Main window
root = tk.Tk()
root.title("To-Do List")

# GUI Components
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=10)

button_add = tk.Button(frame, text="Add Task", command=add_task)
button_add.pack(side=tk.LEFT)

listbox = tk.Listbox(root, height=10, width=45)
listbox.pack(pady=10)

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.pack(pady=10)

# Start the application
root.mainloop()
