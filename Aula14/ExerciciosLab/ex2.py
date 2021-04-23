# Exercício 2:

# Elabore um programa que preencha uma matriz 4x2 com 
# números inteiros recebidos do usuário e mostre essa 
# matriz. Calcule e mostre quantos elementos dessa matriz 
# são maiores que 10 e, em seguida, mostre uma 
# segunda matriz com 0 (zero) no lugar dos elementos 
# maiores que 10. Utilize %3d para imprimir todas as 
# matrizes.

m = []
maiores_dez = []
for i in range(4):
  linha = []
  for j in range(2): 
    valor = int(input("Digite o elemento da linha {} e coluna {}: ".format(i, j)))
    if valor > 10: 
      maiores_dez.append(valor)
    linha.append(valor)
  m.append(linha)

print("Matriz original:")
for i in range(4):
  for j in range(2):
    print("%3d" % m[i][j], end=" ")
  print()

print()
for i in maiores_dez:
  print("{} é maior que 10!".format(i))

print("No total, {} elementos são maiores que 10!".format(len(maiores_dez)))
print()

print("Matriz sem os números maiores que 10:")


for i in range(4):
  for j in range(2):
    if m[i][j] in maiores_dez:
      m[i][j] = 0
    print("%3d" % m[i][j], end=" ")
  print()






