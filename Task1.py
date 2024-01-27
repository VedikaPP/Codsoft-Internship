#Task 1 TO-DO-LIST Given by CodSoft 
#VEDIKA POPAT PHADATARE

import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    global listbox_tasks, entry_task
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(index)
        new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=old_task)
        if new_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def main():
    global listbox_tasks, entry_task
    root = tk.Tk()
    root.title("Task 1 To-Do List")

    frame_tasks = tk.Frame(root)
    frame_tasks.pack(pady=40)

    listbox_tasks = tk.Listbox(frame_tasks,font='Helvetica 10 bold', bg='SlateGray3', width=50, height=5, selectbackground="white")
    listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar_tasks = tk.Scrollbar(frame_tasks, bg='black')
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task = tk.Entry(root,font='Helvetica 10 bold', bg='SlateGray3', width=50)
    entry_task.pack(pady=5)

    button_add_task = tk.Button(root, text="Add Task",font='Helvetica 15 bold', bg='#e8c1c7', command=add_task)
    button_add_task.pack( padx=5)

    button_delete_task = tk.Button(root, text="Delete Task",font='Helvetica 15 bold', bg='#e8c1c7', command=delete_task)
    button_delete_task.pack(side=tk.LEFT, padx=5)

    
    button_edit_task = tk.Button(root, text="Edit Task",font='Helvetica 15 bold', bg='#e8c1c7', command=edit_task)
    button_edit_task.pack(side=tk.RIGHT, padx=5)

    root.config(bg='tomato') 
    root.title('My To-Do-List')
    root.geometry('400x300')
    root.mainloop()
    
if __name__ == "__main__":
    main()