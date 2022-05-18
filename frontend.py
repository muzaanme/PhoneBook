
from operator import index
from tkinter import *
from tkinter import messagebox
from turtle import back
from PIL import Image, ImageTk
from click import command
from pyrsistent import b
from backend import Database


database = Database("contact.db")


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
    except IndexError:
        pass

    
    
def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)
    
def search_command():
    list1.delete(0, END)
    for row in database.search(Name_text.get(), Number.get()):
        list1.insert(END, row)

def add_command():
    if len(Number.get()) == 10:
        database.insert(Name_text.get(), Number.get())
        list1.delete(0, END)
        list1.insert(END, (Name_text.get(), Number.get()))
    else:
        messagebox.showerror("Error", "Please Enter a 10-digit number")

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0], Name_text.get(), Number.get())


window  = Tk()

window.wm_title("PhoneBook")

icon = Image.open('phoneIcon.png')
photo = ImageTk.PhotoImage(icon)
window.wm_iconphoto(False, photo)

#Declaring the Labels
l1 = Label(window, text = "Name")
l1.grid(row = 0, column=0)


l2 = Label(window, text = "Number")
l2.grid(row = 0, column=2)


#Declaring the textBoxes
Name_text = StringVar()
e1 = Entry(window, textvariable = Name_text)
e1.grid(row = 0, column=1)

Number = StringVar()
e2 = Entry(window, textvariable = Number)
e2.grid(row = 0, column=3)




#ListBox (data)

list1 = Listbox(window, height = 7, width = 35)
list1.grid(row = 1, column = 0, rowspan=7, columnspan=2)

#ScrollBar

sb1 = Scrollbar(window)
sb1.grid(row = 1, column=2, rowspan=7)

#list and scrollbar configuration 
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Binds
list1.bind('<<ListboxSelect>>', get_selected_row)


#Buttons

b1 = Button(window, text = "View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text = "Search entry", width=12, command= search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text = "Add entry", width=12, command= add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text = "Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text = "Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text = "Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()