import tkinter
from tkinter import *

top = Tk()
top.geometry("100x100")
top.title('Click me :)')

t = Text(top)
text = 'Hiiii'
# text.place(x=100,y=100)
B = Button(top , text=' Click me')
B.place(x=50,y=50)
top.mainloop()