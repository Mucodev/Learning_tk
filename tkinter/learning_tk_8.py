from os import close
from tkinter import *
from tkinter import messagebox

def save():

    if messagebox.askyesno(title="Save", message= "Do you want to save?"):
        messagebox.showinfo(title="Save", message="Saved")
    else:
        close()
    
def open():
    messagebox.showinfo(title="Open", message="Opened")

def find():
    if messagebox.askyesno(title="Find", message="Do you want to find something?"):
        messagebox.showwarning(title="Something", message="You found Something")
    else:
        messagebox.showwarning(title="Something", message="You didn't find Something")

def copy():
    if messagebox.askyesno(title="Copy", message="Do you want to copy This?"):
        messagebox.showwarning(title="This", message="You copied This")
    else:
        messagebox.showwarning(title="This", message="You didn't copy This")

window = Tk()

window.geometry("300x400")
window.title("Menubar")

openimage= PhotoImage(file="youtube.png").subsample(40,40)

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open, image=openimage, compound=LEFT)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Find", command=find)
editMenu.add_command(label="Copy", command=copy)

window.mainloop()