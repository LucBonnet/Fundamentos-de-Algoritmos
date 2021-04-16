# Exercício 2:

# Faça um programa que cria uma matriz m 10 x 15, sendo que cada elemento 
# é um inteiro gerado aleatoriamente. Então, exiba a matriz completa e, na 
# sequência, somente os elementos da primeira coluna da matriz. 

import random as rdn

m = []

for i in range(10):
  linha = []
  for j in  range(15): 
    linha.append(rdn.randint(0, 100))
  m.append(linha)

print(m)
for linha in range(len(m)):
  print(m[linha][0], end=" ")