from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

# cria o combobox
combobox = Combobox(window)
# insere os possíveis valores
combobox['values'] = (1, 2, 3, 4, 5, 'Text')
# configura o item selecionado
combobox.current(2)
#posiciona o combobox
combobox.place(x=50, y=150)

def show():
  # para ler o valor selecionado
  label['text'] = combobox.get()

btn = Button(window, text="Exibe valor do Combobox", command=show)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label = Label(window)
label.place(x=50, y=170)

window.mainloop()