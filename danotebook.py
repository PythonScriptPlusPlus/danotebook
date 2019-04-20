#from operator import attrgetter
from tkinter import *
#from tkinter import messagebox

class Info:
    def __init__(self,NameW,DateW,PhoneW,DiscW):
        self.NameW = NameW
        self.DateW = DateW
        self.PhoneW = PhoneW
        self.DiscW = DiscW
    
def aDd():
    Person = Info(NameW, DateW, PhoneW, DiscW)
    if read == 'list is clear':
        with open('list.py','w') as f:
            f.write('class Info:\n    def __init__(self,NameW,DateW,PhoneW,DiscW):\n        self.NameW = NameW\n        self.DateW = DateW\n        self.PhoneW = PhoneW\n        self.DiscW = DiscW')            

read = 'test'
tk = Tk()

NameW = StringVar()
DateW = StringVar()
PhoneW = StringVar()
DiscW = StringVar()

tk.title("dank notebook")
with open('list.py','r') as f:
    read = f.read()
    if read == '1' or read == 'class Info:\n    def __init__(self,NameW,DateW,PhoneW,DiscW):\n        self.NameW = NameW\n        self.DateW = DateW\n        self.PhoneW = PhoneW\n        self.DiscW = DiscW':
        read = 'list is clear'

List = Frame(tk, bg = 'black', bd = 1)
addF = Frame(tk, bg = 'black', bd = 1)
delF = Frame(tk, bg = 'black', bd = 1)
modF = Frame(tk, bg = 'black', bd = 1)
name = Frame(tk, bg = 'black', bd = 1)
date = Frame(tk, bg = 'black', bd = 1)
phone = Frame(tk,bg = 'black', bd = 1)
dis1 = Frame(tk,bg = 'black', bd = 1)
dis2 = Frame(tk,bg = 'black', bd = 1)

List.grid(row = 0, column = 1,rowspan = 8)
addF.grid(row = 8, column = 1)
delF.grid(row = 8, column = 2)
modF.grid(row = 8, column = 3)
name.grid(row = 1, column = 2, columnspan = 2)
date.grid(row = 2, column = 2)
phone.grid(row = 3, column = 2)
dis1.grid(row = 4, column = 2)
dis2.grid(row = 5, column = 2, columnspan = 2)

lab = Label(List, text = read, bg = 'white', fg = 'black', height = 14, width = 17)
pic = Label(tk,bg = 'green') 

Name = Entry(name, bg = 'grey', fg = 'black', width = 41, textvariable = NameW)
discName = Label(name, text = "Name, scnd name,\nsurname", width = 42)

Date = Entry(date, bg = 'grey', fg = 'black', width = 20, textvariable = DateW)
discDate = Label(date, text = "date of birth", width = 21)

Phone = Entry(phone, bg = 'grey', fg = 'black', width = 20, textvariable = PhoneW)
discPhone = Label(phone, text = "phone number", width = 21)

Disc = Entry(dis2, bg = 'grey', fg = 'black', width = 41, textvariable = DiscW)
discDisc = Label(dis1, text = "discription", width = 21)

    
mod = Button(modF, text = 'mod', width = 20)
delete = Button(delF, text = 'delete', width = 21)
add = Button(addF, text = 'add', width = 17, command = aDd)

lab.pack()
pic.grid(row = 2, column = 3, rowspan = 5)

Name.grid(row = 1, column = 1, columnspan = 1)
discName.grid(row = 0, column = 1, columnspan = 1)

Date.grid(row = 1, column = 1)
discDate.grid(row = 0, column = 1)

Phone.grid(row = 1, column = 1)
discPhone.grid(row = 0, column = 1)

Disc.grid(row = 0, column = 1, columnspan = 2)
discDisc.grid(row = 0, column = 1)

add.pack()
delete.pack()
mod.pack()
tk.mainloop()
