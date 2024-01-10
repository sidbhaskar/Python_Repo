import tkinter as tk
from tkinter import simpledialog
def check_answer():
    answer = simpledialog.askstring("Question", "Which college has the worst management?")
    if answer == "VIT":
        tk.messagebox.showinfo("Result", "Correct!")
    else:
        tk.messagebox.showerror("Result", "Wrong!")
root = tk.Tk()
button = tk.Button(root, text="Ask", command=check_answer)
button.pack()
root.mainloop()
