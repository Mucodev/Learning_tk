from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="Info Box", message="You were informed")

def virus():
    claim = 0
    while claim < 5:
        messagebox.showwarning(title="Warning!", message="Your computer has virus!!!")
        claim += 1

def error():
    messagebox.showerror(title="Error!", message="Error!!!")         

def do():
    if messagebox.askokcancel(title="Ok-Cancel", message="Do you want to do The Thing? "):
        print("You did The Thing")
    else:
        print("You did not :(")

def do_2():
    
    claim_2 = 1
    
    while claim_2 < 6:
        if messagebox.askretrycancel(title="Try-Cancel", message="Do you want to try or not?"):
            if claim_2 == 1:
                print("You retried 1 time!!")
            elif claim_2 > 1:
                print(f"You retried {claim_2} times!!!")
            claim_2 += 1
        else:
            print("You did not :(")
            break

def yes_no():
    if messagebox.askyesno(title="Yes or No", message= "Are you GAE?"):
        print("YES")
    else:
        print("No is yes for me! That means YOU ARE GAE!!!")

def ask():
    answer = messagebox.askquestion(title="GAE", message="Am I Gae?")

    if answer == "yes":
        print("NO, YOU ARE GAE!!'")
    else:
        print("YOU ARE A HOMOPHOBIC ASSHOLE")

def yes_no_cancel():
    answer = messagebox.askyesnocancel(title="Yes-No-Cancel", message="Yes, No or Cancel ?") # this value is a boolean value!

    if answer == True:
        print("YES")
    elif answer == False:
        print("NO")
    else:
        print("CANCEL")

window = Tk()

button = Button(window, command=click, text="Click Me")
button.pack()

button_2 = Button(window, command=virus, text="Warning")
button_2.pack()

button_3 = Button(window, command=error, text="Error")
button_3.pack()

button_4 = Button(window, command=do, text="ok-cancel")
button_4.pack()

button_5 = Button(window, command=do_2, text="try-cancel")
button_5.pack()

button_6 = Button(window, command=yes_no, text="Yes-No")
button_6.pack()

button_7 = Button(window, command=ask, text="question")
button_7.pack()

button_8 = Button(window, command=yes_no_cancel, text="yes-no-cancel")
button_8.pack()

window.mainloop()