from tkinter import *

# cria a janelas
janela = Tk()

# título para a janela
janela.title("Algoritmos")

# configura o tamanho da janela 
janela.geometry('400x400')

# cria o rótulo na janela desejada, 
# com o texto desejado e configura a fonte
rotulo = Label(janela, text="Primeira aplicação gráfica no Python", font=("Arial Bold", 14))

# configura onde o texto vai aparecer na janela:
# x = 200 e y = 100
# a referência é o centro (CENTER) do rótulo
rotulo.place(x=200, y=100, anchor=CENTER)

# chama a função mainloop: 
# loop infinito para manter a janela aberta
janela.mainloop()

