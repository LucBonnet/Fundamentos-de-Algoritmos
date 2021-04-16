# Listas de Listas ou Listas Aninhadas

# -> Una lista aninhada é uma lista que aparece 
# como um elemento de um outro elemento de uma outra
# lista
# -> O quarto elemento da "lista" (indice 3) é uma 
# lista aninhada
# Ex: lista = ["hello!", 6.7, 5, [1, 2]]
# -> Quando pedimos para imprimir o elemento no índice
# 3, vemos o seguinte
# Ex: print(lista[3])
# Ex: -> [1, 2]

# -> Para acessar o número 2, devemos colocar o índice 3, 
# para acessar a lista aninhada e, depois, o indice 1, para 
# acessar o número 2:
lista = ["hello", 6.7, 5, [1, 2]]
print(lista[3][1])
# -> Os colchetes avaliam a sentença da esq uerda para a direita, 
# então o elemento no indice 3 será acessado primeiro.
# -> Depois, como o elemento no índice 3 é outra lista, podemos 
# acessar o elemento no índice 1, que é o número inteiro
# -> Podemos aninhar listas dentro de listas aninhadas
lista2 = [4, [2, 3], [1, [3, 4]]]
print(lista2[2][1])
print(lista2[2][1][0])
print(lista2[2][1][1])

# Matrizes

# -> Uma matriz é um conjunto (arranjo) com DUAS 
# dimensoes: Linhas e Colunas
# -> Exemplo - matriz A 3x3 (3 linha e 3 colunas)

# -> Matrizes necessitam de duas informações posicionais: 
# São indexadas por linha e coluna

# No Pýthon:

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]
print(a)
print(a[0][2])

# Exemplo: Lendo todos os elementos de uma matriz, um de cada vez
def exemplo1():
  for linha in range(len(a)):
    for coluna in range(len(a)):
      print(a[linha][coluna], end="")

# exemplo1()

# Exemplo:
def exemplo2():
  m = []
  for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
      linha.append(num_linha+num_coluna)
    m.append(linha)
  print(m)

# exemplo2()




