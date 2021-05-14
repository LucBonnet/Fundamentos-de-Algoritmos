# Dicionários:

# -> Dicionários (em Python) são vetores associativos
# -> Vatores associativos são coleções desordenadas de 
# dados, usadas para armazenar valores como um mapa: por
# meio de elementos formados pelo par chave e valor
# -> Assim, diferentemente das listas ou tuplas, que 
# contém um único valor como elemento, o dicionário contém 
# o par chave:valor (key:value)
# # -> Chave (key): serve para deixar o dicionário 
# otimizado
# # -> Valor (value): valor do elemento associado a uma 
# chave
# -> Dicionários diferem das listas essencialmente na 
# meneira como os elementos são acessados:
# # -> Listas: valores são acessados por sua posição dentro 
# da lista, via índice
# # -> Dicionários: valores são acessados por meio de suas 
# chaves

# -> Um dicionário em Python funciona de uma forma 
# semelhante ao dicionário de palavras
# # -> As chaves (keys) de um dicionário devem ser exclusivas e com o tipo de dados imutáveis, como strings, inteiros ou tuplas
# # -> Porém, os valores (values) associados às chaes podem ser repitidos e de qualquer tipo

# -> Para criarmos um dicionário, devemos incluir uma sequência de elementos dentro de chaves {}, separados por vírgula
# -> A chave e o valor são separados por dois pontos
# -> Cada elemento do dicionário é um par composto por chave (key) e valor (value)

def exemplo1():
  d = {
    1: 'exemplo',
    2: 'de',
    3: 'dicionario'
  }

  print(d)

# exemplo1()

# Acessando Elementos

# -> Os valores são acessados por meio de suas chaves
# -> Utiliza-se o nome do dicionário e a chave dentro de colchetes

def exemplo2():
  ingles = {
    'um': 'one',
    'dois': 'two',
    'tres': 'three',
    'quatro': 'four',
    'cinco': 'five'
  }

  print(ingles['um'], ingles['tres'])

# exemplo2()

# Adicionando novos elementos

# -> Para adicionar um novo a um dicionário existente, 
# basta atribuir o novo valor e especificar a chave 
# dentro de colchetes

def exemplo3():
  ingles = {
    'um': 'one',
    'dois': 'two',
    'tres': 'three',
    'quatro': 'four',
    'cinco': 'five'
  }

  ingles['sete'] = 'seven'

  print(ingles['sete'])
  print(ingles)

# exemplo3()

# Removendo elementos:

# -> Para deletar um elemento de um dicionário 
# utilizamos a palavra-chave del

def exemplo4():
  ingles = {
    'um': 'one',
    'dois': 'two',
    'tres': 'three',
    'quatro': 'four',
    'cinco': 'five'
  }

  del ingles['tres']

  print(ingles)

# exemplo4()

# Alguns métodos

# -> items(): retorna todos os elementos do 
# dicionário - pares chave:valor

def exemplo5():
  dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario'
  }

  d = dicionario.items()
  print(d)
  d = list(d)
  print(d)

# exemplo5()

# -> keys(): retorna todas as chaves do dicionário

def exemplo6():
  dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario'
  }

  d = dicionario.keys()
  print(d)
  d = list(d)
  print(d)

# exemplo6()

# -> values(): retorna todos valores do dicionário

def exemplo7():
  dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario'
  }

  d = dicionario.values()
  print(d)
  d = list(d)
  print(d)

# exemplo7()

# Iteração

# -> Podemos utilizar estruturas de repetição para 
# iterar por um dicionário

def exemplo8():
  dicionario = {
    'um': 'exemplo',
    'dois': 'de',
    'tres': 'dicionario'
  }

  for chave in dicionario:
    print(chave)
  
  for valor in dicionario.values():
    print(valor)

  for chave, valor in dicionario.items():
    print(chave)
    print(valor)

# exemplo8()