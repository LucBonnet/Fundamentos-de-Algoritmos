# Exercício 6:

# Crie uma matriz m[12][12] com números inteiros aleatórios.
# Em seguida, calcule e mostre a soma ou a média considerando somente 
# aqueles elementos que estão abaixo da diagonal principal da matriz, 
# conforme ilustrado abaixo (área verde).
# v: verde
# b: branco
# a: amarelo
# a b b b b b b b b b b b
# v a b b b b b b b b b b
# v v a b b b b b b b b b
# v v v a b b b b b b b b 
# v v v v a b b b b b b b
# v v v v v a b b b b b b 
# v v v v v v a b b b b b
# v v v v v v v a b b b b
# v v v v v v v v a b b b
# v v v v v v v v v a b b
# v v v v v v v v v v a b
# v v v v v v v v v v v a

# A entrada do programa deve ser um único 
# caractere maiúsculo 'S' ou 'M', indicando a 
# operação (Soma ou Média) que deverá ser 
# realizada com os elementos da matriz. 

import random as rdn 

operacao = input("Digite a operação desejada: (S/M) ")
m = []
for i in range(12):
  linha = []
  for j in range(12):
    linha.append(rdn.randint(0, 10))
  m.append(linha)

soma = 0
itens = 0
for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    if coluna - linha < 0:
      soma += m[linha][coluna]
      itens += 1

if operacao == 'S':
  print('Soma:', soma)
else:
  print("Média:", soma/itens)

for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    print("%4d" % m[linha][coluna], end=" ")
  print()

      