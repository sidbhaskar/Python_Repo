from tkinter import *
from tkinter.colorchooser import askcolor

top = Tk()
top.geometry('200x200')

def show() :
    color = askcolor()
    print(color)

b = Button(top , text='Color Chooser', command=show)
b.place(x=50 , y=50)

top.mainloop()