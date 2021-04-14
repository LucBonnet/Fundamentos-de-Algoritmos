# Listas

# -> Uma lista é uma variável que armazena um conjunto de valores
# -> é um tipo de variável que permite o armazenamento de valores
# com tipos homogêneos ou heterogêneos (do mesmo tipo ou de tipos 
# diferentes)
# -> Os valores armazenados em uma lista são acessados por um índice
# -> Para indicar que uma variável é uma lista, o símbolo de 
# colchetes [] é utilizado para delimitar o conjunto
# -> Sintaxe - criando uma lista chamada L:
L = []

# Exemplo: criando uma lista z com 3 números inteiros:
def exemplo1():
  z = [5, 7, 1]
  print(z)

# exemplo1()

# -> Dizemos que z tem tamanho 3

# Acesso de elementos

# Exemplo:
def exemplo2():
  z = [5, 7, 1]
  print(z[0]) 
  print(z[1]) 
  print(z[2]) 

# exemplo2()

# -> Utilizando o nome de uma lista com o índice desejado, podemos 
# também modificar o conteúdo armazenado

# Exemplo: Alterando o valor do primeiro elemento da lista z
def exemplo3():
  z = [5, 7, 1]
  z[0] = 32
  print(z)

# exemplo3()

# Fatiamento (Slicing)

# -> No Python, podemos também fatiar as listas, ou seja, pegar 
# somente partes de uma lista

# Exemplo:
def exemplo4():
  p = [1, 2, 3, 4, 5, 6]
  print(p[0:5])
  print(p[:4])
  print(p[1:3])
  print(p[-1])

# exemplo4()

# Adicionando elementos no fim da lista

# -> Podemos ainda adicionar novos elementos no fim da lista
# -> Para isso, utilizamos o método append( item )

# Exemplo:
def exemplo5():
  z = [32, 7, 1]
  print(z)
  z.append("oi")
  print(z)

# exemplo5()

# Adicionando elementos em qualquer lugar da lista

# -> Podemos ainda adicionar novos elementos em qualquer lugar da 
# lista
# -> Para isso, utilizamos o método insert(índice, item)

# Exemplo:
def exemplo6():
  z = [32, 7, 1]
  print(z)
  z.insert(1, "oi")
  print(z)

# exemplo6()

# Removendo da lista pelo índice

# -> Podemos remover um elemento da lista
# -> Para isso, utilizamos o método pop(indice)

# Exemplo:
def exemplo7():
  z = ["a", "b", "c", "d", "e"]
  print(z)
  z.pop(1)
  print(z)

# exemplo7()

# Removendo da lista pelo elemento

# -> Podemos remover um elemento da lista
# -> Para isto, utilizamos o método remove(item)

# Exemplo:
def exemplo8():
  z = ["a", "b", "c", "d", "e"]
  print(z)
  z.remove("d")
  print(z)
  a = [1, 2, 3, 4, 5]
  print(a)
  a.remove(3)
  print(a)

# exemplo8()

# Lista - Cópia

# -> A cópia de uma lista para uma nova variável requer alguma 
# atenção!
# Por exemplo, se quisermos copiar a lista z para uma no variável 
# chamada z1, o mais natural seria: z1=z, mas no Python, isso cria 
# duas variáveis que referenciam a mesma lista
# -> É como se déssemos dois nome para a mesma lista

# Exemplo: 
def exemplo9():
  z = [4, 5, 3, 6]
  z1 = z
  print('z -> ', z)
  print('z1 -> ', z1)
  z[1] = 98
  print('z -> ', z)
  print('z1 -> ', z1)

# exemplo9()

# -> Para criarmos uma cópia independente, utilizamos a sintaxe:

# Exemplo:
def exemplo10():
  z = [4, 5, 3, 6]
  z1 = z[:]
  print('z -> ', z)
  print('z1 -> ', z1)
  z[1] = 98
  print('z -> ', z)
  print('z1 -> ', z1)

# exemplo10()

# Tamanho da lista

# -> Como temos os métodos para incluir e remover dados das listas, 
# nem sempre sabemos qual é o tamnho exato que a lista tem
# -> Para descobrirmos o tamanho da lista, utilizamos o método 
# len(lista)

# Exemplo:
def exemplo11():
  a = [3, 4, 5]
  print(len(a))

  a.append(9)
  a.append(11)
  print(len(a))

# exemplo11()

# Pesquisando na lista

# -> Podemos pesquisar se um elemento está na lista
# -> Par isso, verificamos do primeiro ao último 
# comparando com o que queremos encontrar
# -> Para percorrer listas, utilizamos uma estrutura de repetição:
# while ou for
# A estrutura for é otimizada para trabalhar com listas

# Exemplo:
def exemplo12():
  z = ['a', 'b', 'c', 'd', 'e']
  for item in z:
    if item == "c":
      print("Elemento encontrado!")
      break
  else:
    print('Elemento não encontrado')

# exemplo12()

# -> Porém, se a ideia é somente verficar se o elemento está 
# ou não na lista, podemos utilizar:

# Exemplo:
def exemplo13():
  z = ['a', 'b', 'c', 'd', 'e']
  if 'c' in z:
    print('Encontrado!')
  else:
    print('Não encontrado')

# exemplo13()

# -> Contudo, nem sempre encontrar o elemento é sufucuente
# -> Muitas vezes, precisamos saber qual é a sua posição na lista

# Exemplo:
def exemplo14():
  z = ['a', 'b', 'c', 'd', 'e']
  for indice in range(len(z)):
    if z[indice] == 'c':
      print('Elemento encontrado no índice %d' % indice)
      break
  else:
    print('Elemento não encontrado')

# exemplo14()

# Tuplas

# -> Tuplas são similares às listas, porém são imutáveis
# -> Tuplas não permitem adicionar, apagar, inserir ou modificar 
# elementos
# -> Tuplas são definidas com parênteses () e listas com colchetes []

# Exemplo:
def exemplo15():
  b = (2, 4, 5, 'tupla')
  print(b)
  print(b[1])

# exemplo15()

