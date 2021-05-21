from tkinter import *
from tkinter import messagebox

window = Tk()

def show():
  res = messagebox.showinfo('Aviso', 'O botão de mensagem foi clicado!!')
  print(res)

def show2():
  res = messagebox.askyesno('Mensagem', 'Python é legal?')
  print(res)

def show3():
  res = messagebox.askquestion('Mensagem', 'Mensagem')
  print(res)
  res = messagebox.askyesnocancel('Mensagem', 'Mensagem')
  print(res)
  res = messagebox.askokcancel('Mensagem', 'Mensagem')
  print(res)
  res = messagebox.askretrycancel('Mensagem', 'Mensagem')
  print(res)

btn = Button(window, text='Mensagem 1', command=show)
btn.place(relx=0.5, y=50, anchor=CENTER)

btn2 = Button(window, text='Mensagem 2', command=show2)
btn2.place(relx=0.5, y=100, anchor=CENTER)

btn3 = Button(window, text='Mensagem 3', command=show3)
btn3.place(relx=0.5, y=150, anchor=CENTER)

window.mainloop()