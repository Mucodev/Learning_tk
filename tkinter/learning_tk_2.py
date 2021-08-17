from tkinter import *

window = Tk()

window.geometry("400x640")
window.title("Scale")

scale = Scale(window,
    from_=100,
    to=0, 
    width=20, 
    length=600,
    orient=VERTICAL, #orientation of the scale Horizontal or Vertical
    font=("Consolas", 20),
    tickinterval= 10, # add numeric value to near of the scale
    showvalue=1, # if the value is 0, it doesn't show the current value on the scale 
    resolution=5, # scale will increase 5 by 5 
    troughcolor= "blue",
    fg="green",
    bg="black"
    )
scale.set(0) # this sets the scale stars point to 0 it is not necessary

scale.pack()

def degree():
    print(f"Temperature: {scale.get()} C ")

button = Button(window, command=degree, text="Temperature")
button.pack()

window.mainloop()