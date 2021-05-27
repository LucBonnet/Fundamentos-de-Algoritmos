from tkinter import *
from tkinter import scrolledtext

# cria a janela
window = Tk()
# define um titulo para a janela
window.title('Filtro de Palavras')
# define um tamanho para a janela
window.geometry('900x600')

# Cria as label (palavra, frequência e ocorrências)
lbl_palavra = Label(window, text='Palavra suspeita:', font=('Arial', 14))
lbl_palavra.place(relx=0.05, rely=0.08)

lbl_freq = Label(window, text='Frequência:', font=('Arial', 14))
lbl_freq.place(relx=0.05, rely=0.15)

lbl_ocorre = Label(window, text='Ocorrências:', font=('Arial', 14))
lbl_ocorre.place(relx=0.05, rely=0.3)

# Cria as caixas de texto (palavra e frequência)
txt_palavra = Entry(window, width=15, font=('Arial', 14))
txt_palavra.place(relx=0.25, rely=0.08)

txt_freq = Entry(window, width=15, font=('Arial', 14), state='disable')
txt_freq.place(relx=0.25, rely=0.15)

# Cria a caixa de texto de multiplas linhas
txt = scrolledtext.ScrolledText(window, width=100, height=23, state='disable')
txt.place(relx=0.05, rely=0.35)

# Função que irá pesquisar a palavra digitada
def buscarPalavra():
  # Configura o estado do txt e do txt_freq como normal, ou seja, possível de editar
  txt.configure(state="normal")
  txt_freq.configure(state="normal")

  # Verifica se a caixa de texto não está vazia, caso verdadeiro a caixa de texto será limpada
  if not txt.get(1.0, END) == ' ':
    txt.delete(1.0, END)
  if not txt_freq.get() == ' ':
    txt_freq.delete(0, END)

  # Pega a palavra digitada e a deixa com todas as letras em minusculo
  palavra = txt_palavra.get().lower()

  # Abre o arquivo do chat
  chat = open('chat.txt', 'r')
  # Leitura de todas as linhas do arquivo
  msg = chat.readlines()
  # Fecha o arquivo
  chat.close()

  freq = 0
  # Percorre cada linha do arquivo
  for linha in msg:
    # Remove os espaços e os \n
    linha = linha.strip()
    # Remove os caracteres especiais e deixa tudo em minúsculo
    linha = linha.replace('!', '').replace('?', '').replace('.', '').lower()
    # Separa a linha pelo \t (cada bloco da mensagem, usuário / texto / data / hora)
    linha = linha.split('\t')
    # Verifica se a palavra escolhida está no bloco texto (linha[1])
    if palavra in linha[1].split(' '):
      # Adiciona a linha que contem a palavra na scrolltext
      for p in linha:
        txt.insert(END, p+'*')
      txt.insert(END, '\n\n')
      # Adiciona 1 na frequência
      freq += 1
  # Insere o valor de frequência no campo de texto txt_freq
  txt_freq.insert(0, freq)
  
  # Configura o estado do txt e do txt_freq como disable, ou seja, não editável
  txt_freq.configure(state="disable")
  txt.configure(state="disable")

# Cria o botão de pesquisa
btn_pesquisar = Button(window, text='Pesquisar', font=('Arial', 10), command=buscarPalavra)
btn_pesquisar.place(relx=0.45, rely=0.08)

window.mainloop()