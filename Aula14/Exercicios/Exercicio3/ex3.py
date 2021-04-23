# Escreva uma função que leia uma sequência numérica do arquivo 
# “numeros3.txt” e salva os números na lista num. Esta função deve retornar 
# num. Escreva outra função que recebe a lista num como parâmetro e retorna 
# uma nova lista num_unicos, sem os elementos repetidos. Escreva uma terceira 
# função que recebe a lista num_unicos e grava os números no arquivo 
# “numeros3unicos.txt” 

import random as rdn

def criar_numeros3():
  arquivo = open("numeros3.txt", "w")
  for i in range(100):
    arquivo.write("%d\n" % rdn.randint(0, 100))
  arquivo.close()

num = []
def salvar_valores():
  arquivo = open("numeros3.txt", "r")
  for linha in arquivo.readlines():
    num.append(int(linha.strip()))

num_unicos = []
def unicos(num):
  for i in num:
    if not i in num_unicos:
      num_unicos.append(i)
  print(num_unicos)

def gravar(num_unicos):
  arquivo = open("num_unicos.txt", "w")
  for n in num_unicos:
    arquivo.write("%d\n" % n)
  arquivo.close()

salvar_valores()
unicos(num)
gravar(num_unicos)