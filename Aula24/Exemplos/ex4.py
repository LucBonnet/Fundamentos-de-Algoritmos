from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window, width=10, height=5)
txt.place(relx=0.5, rely=0.5, anchor=CENTER)

def clicked():
  print(txt.get(1.2, END))

btn = Button(window, text="Clique", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()
