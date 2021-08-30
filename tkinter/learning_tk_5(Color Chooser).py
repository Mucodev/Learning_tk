from tkinter import *
from tkinter import colorchooser # submodule
from tkinter import messagebox

window = Tk()

def color():
    color_chooser = colorchooser.askcolor()
    messagebox.showinfo(title="Color", message=f"Color You Choose: {color_chooser[1]}")
    colorHex = color_chooser[1]
    window.config(bg=colorHex)

def color_rgb():
    color_chooser_rgb = colorchooser.askcolor()
    messagebox.showinfo(title="Color", message=f"Color You Choose: {color_chooser_rgb[0]}")
    colorRGB = color_chooser_rgb[1]
    window.config(bg=colorRGB)


window.geometry("420x420")
window.title("Color Chooser")

button = Button(text="Choose a Color(Hex)", command=color)
button.pack()

button_2 = Button(text="Choose a Color(RGB)", command=color_rgb)
button_2.pack()


window.mainloop()