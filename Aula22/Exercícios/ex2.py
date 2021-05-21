# Crie um programa que lê uma letra do alfabeto por 
# uma caixa de texto. Se o usuário digitar a, e, i, 
# o ou u, seu programa deverá exibir uma mensagem 
# indicando que a letra inserida é uma vogal 
# (utilize caixas de mensagem - messagebox). Se o 
# usuário digitar y, seu programa deve exibir uma 
# mensagem indicando que às vezes y é uma vogal 
# (depende da língua, no inglês, por exemplo), e às
# vezes y é uma consoante. Caso contrário, seu 
# programa deve exibir uma mensagem indicando 
# que o letra é uma consoante

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('200x200')

lbl_letra = Label(window, text='Digite uma letra', font=('Arial', 12))
lbl_letra.place(relx=0.5, rely=0.25, anchor=CENTER)

def verficarLetra():
  letra = txt_letra.get()
  letra = letra.lower()
  txt_letra.delete(0, 'end')
  if letra in ['a', 'e', 'i', 'o', 'u']:
    res = messagebox.showinfo('Mensagem', 'A letra inserida é uma vogal')
  elif letra == 'y':
    res = messagebox.showinfo('Mensagem', 'A letra inserida às vezes é uma vogal e às vezes é uma consoante, dependendo da língua')
  elif letra != '':
    res = messagebox.showinfo('Mensagem', 'A letra inserida é uma consoante')
  else:
    res = messagebox.showinfo('Mensagem', 'Digite uma letra')

btn = Button(
  window, 
  text='Verificar',
  font=('Arial', 12),
  width=10,
  height=1,
  bg="#0000ff",
  fg="#fff",
  command=verficarLetra
)
btn.place(relx=0.5, rely=0.75, anchor=CENTER)

txt_letra = Entry(window, font=('Arial', 12), width=15)
txt_letra.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()