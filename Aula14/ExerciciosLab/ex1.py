# Exercício 1:

# Faça um programa que preencha uma matriz M (2x2), 
# solicitando cada elemento (números inteiros) para o 
# usuário. Depois, calcule e mostre uma matriz 
# resultante da multiplicação dos elementos de M pelo 
# seu maior elemento. Utilize %3d para imprimir a matriz.

m = []

maior = 0
for i in range(2):
  linha = []
  for j in range(2): 
    valor = int(input("Digite o elemento da linha {} e coluna {}: ".format(i, j)))
    if valor > maior:
      maior = valor
    linha.append(valor)
  m.append(linha)

print("Matriz resultante:")
for i in range(2):
  for j in range(2):
    m[i][j] = m[i][j] * maior
    print("%3d" % m[i][j], end=" ")
  print()


