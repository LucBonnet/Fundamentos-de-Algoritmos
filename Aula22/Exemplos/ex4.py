from tkinter import *

window = Tk()

window.title("Algoritmos")

window.geometry("400x400")

rotulo = Label(window, text="Primeira aplicação gráfica no Python", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor=CENTER)

entrada = Entry(window, width=14, font=("Arial Bold", 14))
entrada.place(x=200, y=50, anchor=CENTER)

def clique():
  resposta = entrada.get()
  rotulo['text'] = resposta

btn = Button(window, text="Clique!", command=clique)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()