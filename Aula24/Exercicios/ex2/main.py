# Exercício 2

# Uma locadora de veículos te contratou para 
# fazer o aplicativo que controla os aluguéis. 
# Assim, faça uma interface gráfica para 
# cadastro de automóveis (o cadastro deve ser 
# armazenado em arquivo texto). A janela 
# principal deve ter entrada para os seguintes 
# dados

# ● Marca do veículo
# ● Modelo
# ● Ano de fabricação
# ● Placa
# ● Km

# Utilize checkbuttons para os acessórios:
# ● Ar condicionado
# ● Direção hidráulica
# ● Rádio
# ● Airbag

# Além disso, a janela principal deve ter um 
# menu que permita a abertura de outra janela 
# que deve exibir os dados de um veículo por 
# meio de sua placa, em uma área de texto com 
# barra de rolagem.

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

window = Tk()
window.title('Locadora de veículos')
window.geometry('550x200')

menu = Menu(window)
def nova_janela():
  new_window = Tk()
  new_window.title('Buscar veículo')
  new_window.geometry('500x400')
  
  lbl_placa = Label(new_window, text="Placa:", font=("Arial Bold", 14))
  lbl_placa.place(relx=0.15, rely=0.05, anchor=E)

  txt_placa = Entry(new_window, width=10, font=("Arial Bold", 14))
  txt_placa.place(relx=0.18, rely=0.05, anchor=W)

  txt_veiculos = scrolledtext.ScrolledText(new_window, width=55, height=20)
  txt_veiculos.place(relx=0.5, rely=0.5, anchor=CENTER)

  def buscar():
    if not txt_veiculos.get(1.0, END) == ' ':
      txt_veiculos.delete(1.0, END)

    placa = txt_placa.get()
    placa = placa.upper()

    arquivo = open('veiculos.txt', 'r')
    veiculos = arquivo.readlines()
    arquivo.close()

    for i in range(len(veiculos)):
      veiculos[i] = veiculos[i].strip().split('_$_')

      if veiculos[i][5] == '1':
        veiculos[i][5] = 'Ar condicionado'
      else:
        veiculos[i][5] = '-'

      if veiculos[i][6] == '1':
        veiculos[i][6] = 'Direção hidráulica'
      else:
        veiculos[i][6] = '-'

      if veiculos[i][7] == '1':
        veiculos[i][7] = 'Rádio'
      else:
        veiculos[i][7] = '-'

      if veiculos[i][8] == '1':
        veiculos[i][8] = 'Airbag'
      else:
        veiculos[i][8] = '-'

      new_veiculos = []
      for j in range(len(veiculos[i])):
        if not veiculos[i][j] == '-':
          new_veiculos.append(veiculos[i][j])

      veiculos[i] = new_veiculos
      if veiculos[i][3] == placa:
        info = ' | '.join(veiculos[i])
        txt_veiculos.insert(END, info)

  btn = Button(new_window, text="Pesquisar", command=buscar)
  btn.place(relx=0.85, rely=0.05, anchor=CENTER)

menu.add_command(label="Buscar Placa", command=nova_janela)
window.config(menu=menu)

lbl_marca = Label(window, text="Marca do Veículo: ", font=("Arial Bold", 14))
lbl_marca.grid(column=0, row=0, sticky=W)
lbl_modelo = Label(window, text="Modelo: ", font=("Arial Bold", 14))
lbl_modelo.grid(column=0, row=1, sticky=W)
lbl_ano = Label(window, text="Ano de Fabricação: ", font=("Arial Bold", 14))
lbl_ano.grid(column=0, row=2, sticky=W)
lbl_placa = Label(window, text="Placa: ", font=("Arial Bold", 14))
lbl_placa.grid(column=0, row=3, sticky=W)
lbl_km = Label(window, text="Km: ", font=("Arial Bold", 14))
lbl_km.grid(column=0, row=4, sticky=W)

txt_marca = Entry(window, width=20, font=("Arial Bold", 14))
txt_marca.grid(column=1, row=0)
txt_modelo = Entry(window, width=20, font=("Arial Bold", 14))
txt_modelo.grid(column=1, row=1)
txt_ano = Entry(window, width=20, font=("Arial Bold", 14))
txt_ano.grid(column=1, row=2)
txt_placa = Entry(window, width=20, font=("Arial Bold", 14))
txt_placa.grid(column=1, row=3)
txt_km = Entry(window, width=20, font=("Arial Bold", 14))
txt_km.grid(column=1, row=4)

lbl_acessorios = Label(window, text="Acessórios", font=("Arial Bold", 14))
lbl_acessorios.grid(column=2, row=0)

chk_state_ar = BooleanVar()
chk_state_ar.set(False)
chk_ar = Checkbutton(window, text="Ar condicionado", var=chk_state_ar)
chk_ar.grid(column=2, row=1, sticky=W)

chk_state_dh = BooleanVar()
chk_state_dh.set(False)
chk_dh = Checkbutton(window, text="Direção hidráulica", var=chk_state_dh)
chk_dh.grid(column=2, row=2, sticky=W)

chk_state_ra = BooleanVar()
chk_state_ra.set(False)
chk_ra = Checkbutton(window, text="Rádio", var=chk_state_ra)
chk_ra.grid(column=2, row=3, sticky=W)

chk_state_air = BooleanVar()
chk_state_air.set(False)
chk_air = Checkbutton(window, text="Airbag", var=chk_state_air)
chk_air.grid(column=2, row=4, sticky=W)

def cadastrar():
  if chk_state_ar.get():
    ar = '1'
  else:
    ar = '0'

  if chk_state_dh.get():
    dh = '1'
  else:
    dh = '0'

  if chk_state_ra.get():
    ra = '1'
  else:
    ra = '0'

  if chk_state_air.get():
    air = '1'
  else:
    air = '0'

  veiculo = [
    txt_marca.get(),
    txt_modelo.get(),
    txt_ano.get(),
    txt_placa.get(),
    txt_km.get(),
    ar,
    dh,
    ra,
    air
  ]

  veiculo = '_$_'.join(veiculo)

  arquivo = open("veiculos.txt", "a")
  arquivo.write(veiculo+'\n')
  arquivo.close()

  txt_marca.delete(0, END)
  txt_modelo.delete(0, END)
  txt_ano.delete(0, END)
  txt_placa.delete(0, END)
  txt_km.delete(0, END)

  chk_state_ar.set(False)
  chk_state_dh.set(False)
  chk_state_ra.set(False)
  chk_state_air.set(False)


lbl = Label(window)
lbl.grid(column=2, row=5)

btn = Button(window, text="CADASTRAR", command=cadastrar)
btn.grid(column=2, row=6, sticky=E)

window.mainloop()