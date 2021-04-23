# Exercício 3:

# Faça um programa que preencha:

# * Uma lista com 3 nomes de lojas
# * Uma outra lista com 5 nomes de produtos
# * Uma matriz com os preços de todos os produtos em cada loja

# O programa deverá mostrar todas as listas: lojas, produtos 
# e preços (Utilize %3d para imprimir a matriz). Depois, 
# deverá mostrar todas relações (nome do produto – nome da 
# loja - preço) em que o preço não ultrapasse R$ 50,00.

lojas = []
for i in range(3):
  lojas.append(input("Digite o nome da loja: "))

produtos = []
for i in range(5):
  produtos.append(input("Digite o nome do produto: "))

m = []
for i in range(3):
  linha = []
  for j in range(5):
    linha.append(int(input("Digite o preco do produto {0} na loja {1}: ".format(j, i))))
  m.append(linha)

print()
print("Lojas:")
for i in lojas:
  print(i)

print()
print("Produtos:")
for i in produtos:
  print(i)

print()
print("Preços:")
for i in range(len(m)):
  for j in range(len(m[0])):
    print("%3d" % m[i][j], end=" ")
  print()

print()
print("Preços menores que R$ 50.00:")
for i in range(len(m)):
  for j in range(len(m[0])):
    if m[i][j] < 50:
      print("Loja: {0}, produto {1} e preço {2}".format(lojas[i], produtos[j], m[i][j]))
  print()