# Exercício 4:

# Faça um programa para receber uma matriz 3×3 (solicitar ao usuário) e 
# apresentar a soma dos elementos da diagonal principal e a matriz na 
# forma como deve ser vista: com linhas e colunas

m = []

for i in range(3):
  linha = []
  for j in range(3):
    linha.append(int(input("Digite um número: ")))
  m.append(linha)

soma = 0
for i in range(3):
  for j in range(3):
    if i == j:
      soma += m[i][j]

print("Soma:", soma)

for linha in range(3):
  for coluna in range(3):
    print("%4d" % m[linha][coluna], end=" ")
  print()