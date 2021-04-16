# Exercício 7:

# Faça um programa que preencha uma matriz 10x3 com as notas de 10 
# alunos em 3 provas (valores gerados de forma aleatória entre 0 e 10). O 
# programa deverá mostrar:
# a. A matriz com todas as notas de cada aluno
# b. Um relatório com o número do aluno (número da linha), a prova em que 
# cada aluno obteve a menor nota (número da coluna) e o valor da menor 
# nota. 
# c. O relatório deverá mostrar também qual foi a menor nota obtida em cada 
# prova e a quantidade de alunos que obtiveram essa menor nota na 
# respectiva prova.

import random as rdn 

m = []
for i in range(10):
  linha = []
  for j in range(3):
    linha.append(rdn.randint(0, 10))
  m.append(linha)
# a
for linha in range(len(m)):
  for coluna in range(len(m[linha])):
    print("%4d" % m[linha][coluna], end=" ")
  print()

# b
for linha in range(len(m)):
  menor = m[linha][0]
  for coluna in range(len(m[linha])):
    if m[linha][coluna] < menor:
      menor = m[linha][coluna]
  print("Aluno", linha, ", Menor nota:", menor)

# c
menor = 0
qtd = 0
for linha in range(3):
  menor = m[linha][0]
  qtd = 0
  for coluna in range(len(m)):
    if m[coluna][linha] < menor:
      menor = m[coluna][linha]
      qtd = 0
    if m[coluna][linha] == menor:
      qtd += 1
  print("Prova", linha, ", Menor nota:", menor, ", Qtd:", qtd)
