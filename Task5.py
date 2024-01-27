from tkinter import *
from tkinter import messagebox

def update_contact_list():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

def selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

def add_contact():
    if Name.get() and Number.get():
        contactlist.append([Name.get(), Number.get()])
        update_contact_list()
        entry_reset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")

def update_detail():
    if Name.get() and Number.get():
        contactlist[selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        entry_reset()
        update_contact_list()
    elif not(Name.get()) and not(Number.get()) and not(len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill in the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and press Load button")
        else:
            message1 = """To load all information of selected row, press Load button."""
            messagebox.showerror("Error", message1)

def delete_entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[selected()]
            update_contact_list()
    else:
        messagebox.showerror("Error", 'Please select the contact')

def view():
    if len(select.curselection()) != 0:
        name, phone = contactlist[selected()]
        Name.set(name)
        Number.set(phone)
    else:
        messagebox.showerror("Error", "Please select the contact")

def entry_reset():
    Name.set('')
    Number.set('')

def exit_app():
    root.destroy()

root = Tk()
root.geometry('500x600')
root.config(bg='purple')
root.title('My Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Priti Shevte', '9369854712'],
    ['Sakshi Nanaware', '8211552252'],
    ['Asmita Shevte', '8778945614'],
    ['Sharvari Kumbhar', '9958745246'],
    ['Neeta Phadatare', '9165846975'],
    
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame,bg='black', orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16,"bold"), bg="#f0fffc",
                 width=20, height=8, borderwidth=5, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

Label(root, text='Name', font=("Times new roman", 22, "bold"), bg='spring green').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 20, "bold"), bg='spring green').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text=" ADD", font='Helvetica 18 bold', bg='yellow', command=add_contact, padx=20).place(x=50, y=140)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=update_detail, padx=20).place(x=50, y=200)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='crimson', command=delete_entry, padx=20).place(x=50, y=260)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='azure', command=view).place(x=50, y=325)
Button(root, text="RESET", font='Helvetica 18 bold', bg='navy', command=entry_reset).place(x=50, y=390)
Button(root, text="EXIT", font='Helvetica 20 bold', bg='wheat', command=exit_app).place(x=250, y=470)

root.mainloop()
