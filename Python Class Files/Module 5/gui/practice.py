from tkinter import *
from tkinter.colorchooser import askcolor

m = Tk()
m.title('A little title')
m.geometry("500x500")

def show():
    color = askcolor()
    print(color)

B = Button(m, text ="Click", command=show)
B.pack()
m.mainloop()
print("Done .")
