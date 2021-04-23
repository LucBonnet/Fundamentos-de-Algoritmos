# Exercício 4:

# Crie um programa que preencha uma matriz 
# 20x10 (20 linhas e 10 colunas) com números 
# inteiros aleatórios (entre 0 e 10) e some cada 
# uma das linhas, armazenando o resultado das
# somas em um vetor (lista). A seguir, o programa 
# deverá multiplicar cada elemento da matriz 
# pela soma da linha correspondente e mostrar a 
# matriz resultante.

from random import seed
import random as rdn

seed(100)

v = []
soma = 0
m = []
for i in range(20):
  linha = []
  for j in range(10):
    valor = rdn.randint(0, 10)
    soma += valor
    linha.append(valor)
  v.append(soma)
  m.append(linha)

print("Matriz original:")
for i in range(len(m)):
  for j in range(len(m[0])):
    print("%3d" % m[i][j], end=" ")
  print()

print()
print("Vetor com a somatória de cada linha:")
print(v)

print()
print("matriz depois da multiplicação:")
for i in range(len(m)):
  for j in range(len(m[0])):
    m[i][j] *= v[i]
    print("%5d" % m[i][j], end=" ")
  print()