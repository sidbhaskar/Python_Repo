from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry('200x200')


def show():
    string = askstring("Input", "Input an String")
    print(string)


B = Button(top, text='Click', command=show)
B.place(x=50, y=50)
top.mainloop()
