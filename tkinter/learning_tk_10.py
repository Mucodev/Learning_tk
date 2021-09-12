from tkinter import *

def new():
    new_window = Toplevel()     # it is associated with bottom window, if you close the bottom window it will close too
                                # This is a top window
                                
                            
    new_window.title("New Window (Toplevel)")
    new_window.geometry("200x200")

def newTk():
    new_window = Tk()     # Tk() is creating a new independent window
                                
                            
    new_window.title("New Window (Tk)")
    new_window.geometry("200x200")    

def newD():
    new_window = Tk()     
                                
                            
    new_window.title("New Window (D)")
    new_window.geometry("200x200")

    window.destroy()

window = Tk() # This is a bottom window

window.geometry("300x400")
window.title("Create a new window")

button_1 = Button(window, text="New Window(Toplevel)", command=new)
button_1.pack()

button_2 = Button(window, text="New Window(Tk)", command=newTk)
button_2.pack()

button_2 = Button(window, text="New Window(D)", command=newD)
button_2.pack()

window.mainloop()