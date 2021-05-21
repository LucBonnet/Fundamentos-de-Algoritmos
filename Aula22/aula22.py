# GUI - Graphical User Interface

# -> Intercae Gráfica do Usuário
# -> Foco no usuário final
# # -> Mais amigavel
# # -> Interação mais rápida
# # -> Mais produtiva

# Frameworks para Python:
# -> Tkinter (Tk interface)
# # -> Toolkit padrão do Python para desenvolvimento de GUI
# -> PyQt
# -> wxPython

# -> O Tkinter permite a criação de janelas, rótulos, 
# botões, caixas de texto, caixas de mensagem, etc.

# Posicionamento dos Elementos

# -> O place permite que os elementos sejam 
# explicitamente posicionados de forma absoluta ou 
# relativa

# Posicionando o elemento w, de forma relativa (centralizando):
# w.place(relx=0.5, rely=0.5, anchor=CENTER)

# Posicionando o elemento w de forma absoluta
# w.place(x=50, y=100, anchor=CENTER)

# -> anchor refere-se ao elemento que está sendo posicionado:
# # -> Pode assumir os valores:
# # # -> NW (default), N, NE, E, SE, S, SW, W, CENTER

# Botão (Button)

# -> O botão deve ser associado à uma função

# Caixa de Texto (Entry)

# entrada = Entry(janela, width=14, font=("Arial Bold", 14))
# entrada.place(x=200, y=50, anchor=CENTER)

# Caixa de Mensagem (MessageBox)

# exemplo 5 -> ex5.py
