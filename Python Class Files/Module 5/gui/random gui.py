from tkinter import *
from tkinter.colorchooser import askcolor

m = Tk()
m.geometry('200x100')

def show():
    color = askcolor()
    print(color)

B = Button(m,text='Click Me', command=show)
B.place(x=50,y=50)
m.mainloop()