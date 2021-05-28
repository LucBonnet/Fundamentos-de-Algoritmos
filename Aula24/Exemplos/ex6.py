from tkinter import *

window = Tk()
window.title('Algoritmos')
window.geometry('350x200')

rotulo = Label(window, text="Contador: ", font=('Arial Bold', 20))
rotulo.place(relx=0.5, y=100, anchor=E)

rotulo2 = Label(window, text=": ", font=('Arial Bold', 20))
rotulo2.place(relx=0.5, y=100, anchor=W)

k = 0

def loop_function():
  global k
  k += 1
  rotulo2['text'] = k
  window.after(1000, loop_function)

loop_function()
window.mainloop()