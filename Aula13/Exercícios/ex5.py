# Exercício 5:

# Faça um programa que cria uma matriz A 10x5 com números inteiros 
# aleatórios e, então, exiba a matriz transposta de A ( A^t ). 

# Determinar a transposta de uma matriz é reescrevê-la de forma que suas 
# linhas e colunas troquem de posições ordenadamente, isto é, a primeira 
# linha é reescrita como a primeira coluna, a segunda linha é reescrita 
# como a segunda coluna e assim por diante, até que se termine de 
# reescrever todas as linhas na forma de coluna.

import random as rdn

m = []
for i in range(10):
  linha = []
  for j in range(5):
    linha.append(rdn.randint(0, 100))
  m.append(linha)

new_m = []
for i in range(5):
  linha = []
  for j in range(10):
    linha.append(m[j][i])
  new_m.append(linha)

print("Matriz:")
for linha in range(10):
  for coluna in range(5):
    print("%4d" % m[linha][coluna], end=" ")
  print()
print("Matriz transposta:")
for linha in range(5):
  for coluna in range(10):
    print("%4d" % new_m[linha][coluna], end=" ")
  print()