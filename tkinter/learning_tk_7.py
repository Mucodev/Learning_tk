from tkinter import *
from tkinter import filedialog

window = Tk()

window.geometry("640x450")
window.title("FileDialog")

def save():
    file = filedialog.asksaveasfile(
        initialdir="C:\\Users\\Mücahit TAlha\\Desktop\\tkinter",
        defaultextension=".txt",
        filetypes=[
            ("Text file", ".txt"),
            ("HTML file", ".html"),
            ("All files", ".*")
        ])
    
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()
    

def dialog():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Mücahit TAlha\\Desktop\\tkinter",
        title="Open file",
        filetypes= (("text files","*.txt",),("all files","*.*")),
        )
    file = open(filepath, "r")
    print(file.read())
    file.close()

button = Button(window, text="File Dialog", command=dialog)
button.pack()

text = Text(window,)
text.pack()

button_2 = Button(window, text="Save", command=save)
button_2.pack()


window.mainloop()