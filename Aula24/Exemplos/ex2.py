from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

# cria a variável de estado
chk_state = BooleanVar()
# configura o estado
chk_state.set(False)
# cria a variável de estado
chk_state2 = BooleanVar()
# configurao estado
chk_state2.set(True)
# cria o checkbutton
chk = Checkbutton(window, text="Texto 1", var=chk_state)
chk2 = Checkbutton(window, text="Texto2", var=chk_state2)
chk.place(x=50, y=100)
chk2.place(x=50, y=130)

def show():
  label['text'] = chk_state.get()

btn = Button(window, text="Exibe valor do checkbutton 1", command=show)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)

label = Label(window)
label.place(x=50, y=170)

window.mainloop()