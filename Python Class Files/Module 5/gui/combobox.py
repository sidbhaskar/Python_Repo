from tkinter import *
from tkinter import ttk

top = Tk()
top.geometry("200x200")

frame = Frame(top)
frame.pack()

langs = ['C','C++','Java','Python']
Combo = ttk.Combobox(frame, values=langs)
Combo.set('Choose your language')
Combo.pack(padx=5,pady=5)
top.mainloop()


