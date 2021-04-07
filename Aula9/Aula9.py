## Funções

# ->  São blocos de código que realizam determinadas tarefas que normalmente 
# precisam ser executadas diversas vezes dentro da mesma aplicação

# -> Assim, tarefas muito utilizadas costumam ser agrupadas em funções, que, depois de 
# definidas, podem ser utilizadas/chamadas em qualquer parte do código somente
# pelo seu nome

# -> Invocar/chamar uma função pode ser visto como uma contratação de uma pessoa 
# para executar um trabalho específico. Ex: função para organizar papéis e livros

# No Python: Funções - def

# -> Podemos criar/definir nossas próprias funções no python utilizando a 
# palavra-chave def seguido do nome da função, parênteses () e :

# Ex:
# def soma(a, b):
#   print(a + b)

# Funções com e sem parâmetros

# -> As funções podem ou não ter parâmetros, que são valores eviados às funções 
# dentro dos parênteses no momento em que elas são chamadas

# Ex:
# Sem parâmetros
# def soma():
#   a = 9
#   b = 8
#   print(a+b)

# Com parâmetros
# def soma(a, b):
#   print(a + b)
#
# soma(3, 4)

# Return

# -> Além dos parâmetros, as funções podem ou não ter um valor de retorno
# -> O retorn é definido pela palavra-chave return

# Ex:
# Sem parâmetros
# def soma():
#   a = 9
#   b = 8
#   return (a + b)
#
# print(soma())

# Ex: 
# Com parâmetros
# def soma(a, b):
#   return (a + b)
#
# print(soma(3, 4))

# Exemplo: Fazer uma função que retorne True ou False para a verificação de 
# números pares

def par(num):
  return (num % 2 == 0)

# print(par(3))
# print(par(4))
# print(par(67))

# Exemplo: Se precisarmos de uma função que retorne a string "par" ou "ímapar",
# podemos reutilizar a função par e criar uma função nova:

def parOuImpar(x):
  if par(x):
    return "par!"
  else:
    return "ímpar!"

# print(parOuImpar(4))
# print(parOuImpar(3))
# print(parOuImpar(56))

# Escopo das variáveis: locais Vs. globais

# -> Quando usamos funções, trabalhamos com variáveis internas, que pertencem 
# somente a função
# -> Estas variáveis internas são chamadas variáveis locais
# -> Não podemos acessar os valores das variáveis locais fora da função a que 
# elas pertencem
# -> É por isso que passamos parâmetros e retornamos valores das funções. Os 
# parâmetros e o return possibilitam a troca de dados no programa

# -> Por sua vez, as variáveis globais são definidas fora das funções e podem ser 
# vistas e acessadas por todas as funções e pelo "código principal" (que não está
# dentro de uma função específica)

# Ex:
a = 5

def alteraValor():
  a = 7
  print("Dentro da função 'a' vale:", a)

# print("'a' antes da chamada da função:", a)
# alteraValor()
# print("'a' depois da chamada da função:", a)

# -> Se quisermos modificar a variável global dentro da função, devemos utilizar 
# a palavra-chave global

# Ex:
a = 5

def alteraValor2():
  global a
  a = 7
  print("Dentro da função 'a' vale:", a)
  
# print("'a' antes da chamada da função:", a)
# alteraValor2()
# print("'a' depois da chamada da função:", a)

# Parâmeros Opcionais

# -> Podemos ainda criar funções que podem ou não receber argumentos

# Ex: 
def soma(a=1, b=1):
  print(a+b)

# # Na chamada sem argumentos, soma assume valores 1 para 'a' e 'b'
# soma()
# # Na chamada com argumentos, soma assume os valores passados
# soma(2, 3)

# Função lambda

# -> No Python, podemos criar funções simples em somente um linha
# -> Estas funções, ou expressões, são chamadas de lambda

# Exempolo: função lambda que recebe um parâmetro x e retorna o quadrado desse 
# número

a = lambda x : x**2
# print(a(3))

# Exemplo: função lambda que calcula o aumento, dado o valor inicial e a 
# porcentagem de aumento

aumento = lambda a, b : (a*b) / 100
# print(aumento(100, 5))