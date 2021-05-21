from tkinter import *

window = Tk()

window.title("Algoritmos")

window.geometry("400x400")

rotulo = Label(window, text="Primeira aplicação gráfica no Python", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor=CENTER)

def clique():
  rotulo['text'] = 'Novo texto'

btn = Button(window, text="Clique!", command=clique)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()