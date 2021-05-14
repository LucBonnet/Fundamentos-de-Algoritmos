# Exercício 5:

# Um cartão de bingo consiste de 5 colunas de 5 
# números. As colunas são rotuladas com as 
# letras B, I, N, G e O. Existem 15 números que 
# podem aparecer na coluna de cada letra. Em 
# particular, os números que podem aparecer na 
# coluna de B estão no intervalo de 1 a 15, os 
# números que podem aparecer sob o I variam de 
# 16 a 30 e assim por diante. Escreva uma função 
# que cria um cartão de Bingo com números 
# aleatórios e armazena tudo em um dicionário. 
# As chaves serão as letras B, I, N, G e O. Os 
# valores serão as listas de cinco números que 
# aparecem em cada letra. Escreva uma segunda 
# função que exibe o cartão de Bingo com as 
# colunas identificadas adequadamente. Use estas 
# funções para escrever um programa que exibe
# um cartão aleatório

import random as rdn

def criaCartela():
  dic = {
    'B': [],
    'I': [],
    'N': [],
    'G': [],
    'O': []
  }

  i = 0
  for chave in dic:
    lista = []
    for j in range(5):
      num = rdn.randint(1 + (15*i), 15 + (15*i))
      while num in lista:
        num = rdn.randint(1 + (15*i), 15 + (15*i))
      lista.append(num)
    lista.sort()
    dic[chave] = lista
    i += 1
  
  return dic

def mostraCartela(cartela):
  car = []

  car.append(list(cartela.keys()))

  for i in range(5):
    linha = []
    for chave in cartela:
      linha.append(cartela[chave][i])
    car.append(linha)
  
  for i in range(len(car)):
    for j in range(len(car[0])):
      print("%4s" % car[i][j], end=" ")
    print()

    

def main():
  cartela = criaCartela()
  mostraCartela(cartela)

main()