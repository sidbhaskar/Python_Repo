import tkinter

m = tkinter.Tk()
m.title('A very little title')
button = tkinter.Button(m,text="Stop",width=15, command=m.destroy)
button.pack()
m.mainloop()