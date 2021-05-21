# Faça uma calculadora para transformar números 
# decimais em: binários, hexadecimais ou octais. 
# Cada base numérica deve ter um botão para 
# realizar a conversão.

from tkinter import *

window = Tk()

window.geometry('400x200')
window.title('Conversão numérica')

def btn_bin_action():
  valor = int(txt_Numero.get())
  txt_Resp.delete(0, 'end')
  txt_Resp.insert(0, bin(valor))

def btn_hex_action():
  valor = int(txt_Numero.get())
  txt_Resp.delete(0, 'end')
  txt_Resp.insert(0, hex(valor))

def btn_oct_action():
  valor = int(txt_Numero.get())
  txt_Resp.delete(0, 'end')
  txt_Resp.insert(0, oct(valor))

lbl_Numero = Label(window, text='Número decimal:', font=('Arial', 14))
lbl_Resp = Label(window, text='Resposta:', font=('Arial', 14))

btn_bin = Button(window, text='Binário', command=btn_bin_action)
btn_hex = Button(window, text='Hexadecimal', command=btn_hex_action)
btn_oct = Button(window, text='Octal', command=btn_oct_action)

txt_Numero = Entry(window, width=14, font=("Arial Bold", 14))
txt_Resp = Entry(window, width=14, font=("Arial Bold", 14))

lbl_Numero.place(relx=0.25, rely=0.25, anchor=CENTER)
lbl_Resp.place(relx=0.30, rely=0.75, anchor=CENTER)

btn_bin.place(relx=0.2, rely=0.5, anchor=CENTER)
btn_hex.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_oct.place(relx=0.8, rely=0.5, anchor=CENTER)

txt_Numero.place(relx=0.75, rely=0.25, anchor=CENTER)
txt_Resp.place(relx=0.75, rely=0.75, anchor=CENTER)

window.mainloop()

