# Exercício 8:

# Define-se o elemento MINIMAX de uma matriz como sendo o maior elemento 
# da linha onde se encontra o menor elemento da matriz. Elabore um programa 
# que carregue uma matriz 4x7 com números reais, calcule e mostre seu 
# MINIMAX e sua posição (linha e coluna). 

import random as rdn 

m = []
for i in range(4):
  linha = []
  for j in range(7):
    linha.append(round(rdn.random() * 100, 2))
  m.append(linha)

for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    print("%4f" % m[linha][coluna], end=" ")
  print()

menor = m[0][0]
linha = 0
for i in range(len(m)):
  for j in range(len(m[i])):
    if m[i][j] < menor:
      menor = m[i][j]
      linha = i

maior = m[linha][0]
coluna = 0
for j in range(len(m[linha])):
  if m[linha][j] > maior:
    maior = m[linha][j]
    coluna = j

print("MINIMAX:", maior, "({0}, {1})".format(linha, coluna))