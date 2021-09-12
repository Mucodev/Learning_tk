from tkinter import *
from tkinter import messagebox

def w():
    messagebox.showinfo(title="W", message="You pressed 'W'")
def a():
    messagebox.showinfo(title="A", message="You pressed 'A'")
def s():
    messagebox.showinfo(title="S", message="You pressed 'S'")
def d():
    messagebox.showinfo(title="D", message="You pressed 'D'")

window = Tk()

window.geometry("640x420")
window.title("Frames")

frame = Frame(window, bg="yellow", border=5, relief=SUNKEN, padx=15, pady=15)
frame.pack(side=BOTTOM) # TOP, BOTTOM, LEFT, RİGHT 
                        # Can be used with ".place()"

button_w = Button(frame, text="W", font=("Consolas", 25), width=3, border=5, relief=RAISED, command=w)
button_w.pack(side=TOP)
button_a = Button(frame, text="A", font=("Consolas", 25), width=3, border=5, relief=RAISED, command=a)
button_a.pack(side=LEFT)
button_s = Button(frame, text="S", font=("Consolas", 25), width=3, border=5, relief=RAISED, command=s)
button_s.pack(side=LEFT)
button_d = Button(frame, text="D", font=("Consolas", 25), width=3, border=5, relief=RAISED, command=d)
button_d.pack(side=LEFT)

window.mainloop()