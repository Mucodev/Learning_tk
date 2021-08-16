from tkinter import *
from tkinter.font import BOLD
from typing import Sized

window = Tk()

window.geometry("640x400")
window.title("Youtube Downloader")

icon = PhotoImage(file="youtube.png").subsample(16, 16)



window.iconphoto(True, icon)

window.config(bg="#E7F5F7")

label = Label(
    window, 
    text="Youtube Downloader", 
    font=("Arial", 20, "bold"), 
    background="#E7F5F7", 
    foreground="#262526",
    relief=RAISED,
    bd=10,
    padx=5,
    pady=5,
    image=icon,
    compound=LEFT,
    )
label.pack()
# label.place(x=0, y=100)

label_2 = Label(window,
    text="Paste the link here: ",
    font=("Arial", 10, "bold"),
    background="#E7F5F7", 
    foreground="#262526")
label_2.place(relx=0, rely=0.25)

d_icon = PhotoImage(file="download.png",).subsample(8,8)

# button.place(x=530, y=70)
links = Entry(window,
    font=("Arial", 10),
)

# links.config(show="*")

links.place(relx=0, rely=0.3, relwidth=1)

def click():
    link = links.get()
    print(f"Here is the link: {link}")

def delete():
    links.delete(0,END)

def backspace():
    links.delete(len(links.get())-1, END)


button = Button(window,
    text="Download",
    command=click,
    font=("Comic Sans", 10),
    fg="#262526",
    bg="#E7F5F7",
    activeforeground="#262526",
    activebackground="#E7F5F7",
    image= d_icon,
    compound=LEFT,
    padx=2,
    pady=2
    )

button.place(relx=0, rely=0.35, relwidth=0.15, relheight=0.1)



button_delete = Button(window,
    text="Delete ",
    command=delete,
    fg="#262526",
    bg="#E7F5F7",
    activeforeground="#262526",
    activebackground="#E7F5F7"
)
button_delete.place(relx=0.151, rely=0.35, relwidth=0.1, relheight=0.1)

button_backspace = Button(window,
    text="Backspace",
    command=backspace,
    fg="#262526",
    bg="#E7F5F7",
    activeforeground="#262526",
    activebackground="#E7F5F7"
)
button_backspace.place(relx=0.251, rely=0.35, relwidth=0.1, relheight=0.1)

x = IntVar()

def display():
    if (x.get()==1):
        print("You agree!")
    else:
        print("You don't agree!")

check_button = Checkbutton(window, text="It's a check button", bg="#E7F5F7", activebackground="#E7F5F7",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display)

check_button.place(relx=0, rely=0.45)

x = IntVar()

def quality():
    if (x.get() == 1):
        print("144")
    elif (x.get() == 2):
        print("240")
    elif (x.get() == 3):
        print("360")
    elif (x.get() == 4):
        print("480")
    elif (x.get() == 5):
        print("720")
    elif (x.get() == 6):
        print("1080")
    elif (x.get() == 7):
        print("1440")
    elif (x.get() == 8):
        print("2160")

radio_button_1 = Radiobutton(window, text="144", variable=x, value=1, indicatoron=0, command=quality)
radio_button_1.place(relx=0, rely=0.5)

radio_button_2 = Radiobutton(window, text="240", variable=x, value=2, indicatoron=0, command=quality)
radio_button_2.place(relx=0.04, rely=0.5)

radio_button_3 = Radiobutton(window, text="360", variable=x, value=3, indicatoron=0, command=quality)
radio_button_3.place(relx=0.08, rely=0.5)

radio_button_4 = Radiobutton(window, text="480", variable=x, value=4, indicatoron=0, command=quality)
radio_button_4.place(relx=0.12, rely=0.5)

radio_button_5 = Radiobutton(window, text="720", variable=x, value=5, indicatoron=0, command=quality)
radio_button_5.place(relx=0.16, rely=0.5)

radio_button_6 = Radiobutton(window, text="1080", variable=x, value=6, indicatoron=0, command=quality)
radio_button_6.place(relx=0.20, rely=0.5)

radio_button_7 = Radiobutton(window, text="1440", variable=x, value=7, indicatoron=0, command=quality)
radio_button_7.place(relx=0.25, rely=0.5)

radio_button_8 = Radiobutton(window, text="2160", variable=x, value=8, indicatoron=0, command=quality)
radio_button_8.place(relx=0.30, rely=0.5)

window.mainloop()