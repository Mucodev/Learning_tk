from tkinter import *

def order():
    
    requested = []

    for a in list_box.curselection():
        requested.insert(a, list_box.get(a))
        
    for b in requested:   
        print(f"You have ordered {b.title()}")

def entry():
    a = entry_box.get()
    list_box.insert(list_box.size(), a)
    list_box.config(height=list_box.size())

def delete():
    for d in reversed(list_box.curselection()):
        list_box.delete(d)
    list_box.config(height=list_box.size())

window = Tk()

window.geometry("640x400")

list_box = Listbox(window,
    bg="gray",
    foreground="green",
    font=("Arial", 20),
    width=12,
    selectmode=MULTIPLE)

list_box.insert(1, "pizza")
list_box.insert(2, "pasta")
list_box.insert(3, "garlic bread")
list_box.insert(4, "soup")
list_box.insert(5, "salad")

list_box.pack()

list_box.config(height=list_box.size())

order_button = Button(window, text="Order", command=order)
order_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()


entry_box = Entry(window)
entry_box.pack()

entry_button = Button(window, text="Enter", command=entry)
entry_button.pack()


window.mainloop()