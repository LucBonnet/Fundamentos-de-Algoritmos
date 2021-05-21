from tkinter import *

window = Tk()

window.title("Algoritmos")

window.geometry("350x200")

btn = Button(window, text="Clique!")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

btn2 = Button(window, text="Clique2!")
btn2.place(x=100, y=50, anchor=CENTER)

window.mainloop()