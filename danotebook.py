from tkinter import *

read = 'test'
tk = Tk()
with open('list.txt','r') as f:
    read = f.read()
    if read == '1':
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

mod = Button(modF, text = 'mod', width = 20)
delete = Button(delF, text = 'delete', width = 21)
add = Button(addF, text = 'add', width = 17)

Name = Entry(name, bg = 'grey', fg = 'black', width = 41)
discName = Label(name, text = "Name, scnd name,\nsurname", width = 42)

Date = Entry(date, bg = 'grey', fg = 'black', width = 20)
discDate = Label(date, text = "date of birth", width = 21)

Phone = Entry(phone, bg = 'grey', fg = 'black', width = 20)
discPhone = Label(phone, text = "phone number", width = 21)

Disc = Entry(dis2, bg = 'grey', fg = 'black', width = 41)
discDisc = Label(dis1, text = "discription", width = 21)

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
