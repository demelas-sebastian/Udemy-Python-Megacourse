from tkinter import *
from backend import Database

db=Database('boooks.db')

def get_selected_row(event):
    global selected_tuple
    try:
        index=box.curselection()[0]
        selected_tuple=box.get(index)
        e_author.delete(0,END)
        e_title.delete(0,END)
        e_year.delete(0,END)
        e_isbn.delete(0,END)
        e_title.insert(END,selected_tuple[1])
        e_author.insert(END,selected_tuple[2])
        e_year.insert(END,selected_tuple[3])
        e_isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    box.delete(0,END)
    for row in db.view():
        box.insert(END,row)

def search_command():
    box.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        box.insert(END,row)

def add_command():
    db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    box.delete(0,END)
    box.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    db.update(selected_tuple[0],e_title.get(),e_author.get(),e_year.get(),e_isbn.get())
    box.delete(0,END)
    for row in db.view():
        box.insert(END,row)

def delete_command():
    db.delete(selected_tuple[0])
    box.delete(0,END)
    for row in db.view():
        box.insert(END,row)

window=Tk()
window.wm_title('BookStore')

l_title=Label(window,text='Title')
l_author=Label(window,text='Author')
l_year=Label(window,text='Year')
l_isbn=Label(window,text='ISBN')
l_title.grid(row=0,column=0)
l_author.grid(row=0,column=2)
l_year.grid(row=1,column=0)
l_isbn.grid(row=1,column=2)

title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
isbn_text=StringVar()
e_title=Entry(window,textvariable=title_text)
e_author=Entry(window,textvariable=author_text)
e_year=Entry(window,textvariable=year_text)
e_isbn=Entry(window,textvariable=isbn_text)
e_title.grid(row=0,column=1)
e_author.grid(row=0,column=3)
e_year.grid(row=1,column=1)
e_isbn.grid(row=1,column=3)

box=Listbox(window,height=6,width=35)
box.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll_box=Scrollbar(window)
scroll_box.grid(row=2,column=2,rowspan=6)

box.configure(yscrollcommand=scroll_box.set)
scroll_box.configure(command=box.yview)

box.bind('<<ListboxSelect>>',get_selected_row)

b_view=Button(window,text='View all',command=view_command,width=12)
b_search=Button(window,text='Search entry',command=search_command,width=12)
b_add=Button(window,text='Add entry',command=add_command,width=12)
b_update=Button(window,text='Update',command=update_command,width=12)
b_delete=Button(window,text='Delete',command=delete_command,width=12)
b_close=Button(window,text='Close',command=lambda x=window:db.close(x),width=12)
b_view.grid(row=2,column=3)
b_search.grid(row=3,column=3)
b_add.grid(row=4,column=3)
b_update.grid(row=5,column=3)
b_delete.grid(row=6,column=3)
b_close.grid(row=7,column=3)

window.mainloop()
