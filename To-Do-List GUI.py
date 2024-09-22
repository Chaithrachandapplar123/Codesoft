import tkinter as tk
from tkinter import messagebox
import json

tasks = []
def add_task():
    task_description = task_entry.get()
    if task_description:
        task = {'description': task_description, 'completed': False}
        tasks.append(task)
        task_list.insert(tk.END, task_description)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")


# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = task_list.curselection()[0]
        tasks[selected_task_index]['completed'] = True
        task_list.itemconfig(selected_task_index, {'fg': 'green'})
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")


# Function to save tasks to a file
def save_tasks():
    with open('tasks_gui.json', 'w') as f:
        json.dump(tasks, f)
    messagebox.showinfo("Success", "Tasks saved successfully!")


# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open('tasks_gui.json', 'r') as f:
            tasks = json.load(f)
        for task in tasks:
            task_list.insert(tk.END, task['description'])
            if task['completed']:
                task_list.itemconfig(tk.END, {'fg': 'green'})
    except FileNotFoundError:
        messagebox.showinfo("Info", "No saved tasks found.")


# Set up the main application window
root = tk.Tk()
root.title("To-Do List")

# Set up the task input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Set up the task list frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_list = tk.Listbox(task_frame, height=10, width=50)
task_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Set up the task action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=5)

# Load any saved tasks on startup
load_tasks()

# Start the Tkinter event loop
root.mainloop()

