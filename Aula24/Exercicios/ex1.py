# Exercício 1

# Construa um relógio digital que atualize a 
# cada 1 segundo e exiba, 
# além da hora, o dia, mês e ano.
# * utilize o pacote datetime

from tkinter import *
from datetime import *

window = Tk()
window.title('Exercício 1')
window.geometry('300x200')

lbl_h = Label(window, text="", font=("Arial Bold", 20))
lbl_h.place(relx=0.5, rely=0.25, anchor=CENTER)

lbl_d = Label(window, text="", font=("Arial bold", 20))
lbl_d.place(relx=0.5, rely=0.75, anchor=CENTER)

datahora = 0

def loop_function():
  global datahora
  datahora = datetime.now()
  data = datahora.strftime('%d/%m/%Y')
  lbl_d['text'] = data
  hora = datahora.strftime('%H:%M:%S')
  lbl_h['text'] = hora
  window.after(1000, loop_function)

loop_function()
window.mainloop()