from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

selected = IntVar()

rad1 = Radiobutton(window, text='Um', value = 1, variable=selected)
rad2 = Radiobutton(window, text='Dois', value = 2, variable=selected)
rad3 = Radiobutton(window, text='Três', value = 3, variable=selected)

rad1.place(x=10, y=50)
rad2.place(x=10, y=100)
rad3.place(x=10, y=150)

def cliqued():
  print(selected.get())

btn = Button(window, text="Clique", command=cliqued)
btn.grid(column=0, row=3)

window.mainloop()