# Exercício 1:

# Faça um programa que leia uma quantidade de números que será digitada 
# pelo usuário. Em seguida, digite todos os números, conforme quantidade
# digitada, e informe o maior deles.

def ex1():
  # entrada da quantidade de números que irão ser digitados
  qtd_de_numeros = int(input("Entre com a quantidade de números que serão digitados: "))
   
  maior_numero = 0
  for i in range(qtd_de_numeros):
    numero = int(input("{0}º número : ".format(i+1)))
    if maior_numero == 0:
      maior_numero = numero
    if numero > maior_numero:
      maior_numero = numero

  print("Maior número digitado:", maior_numero)

# Exercício 2:

# Escreva um programa que exiba uma tabela de conversão de temperatura de 
# graus Celsius para graus Fahrenheit. A tabela deve incluir linhas para 
# todas as temperaturas (de 5 em 5 graus Celsius ) entre um valor inteiro 
# mínimo e um valor inteiro máximo (incluso) digitados pelo usuário. Inclua 
# cabeçalhos apropriados em suas colunas. A fórmula para conversão entre 
# graus Celsius e graus Fahrenheit pode ser encontrada na internet.

def ex2():
  valor_minimo = int(input("Digite o valor mínimo em graus C: "))
  valor_maximo = int(input("Digite o valor máximo em graus C: "))

  print("  Temperatura em C   Temperatura em F")

  # valor_c : valor em C
  # valor_f : valor em F
  for valor_c in range(valor_minimo, valor_maximo+1, 5):
    valor_f = (9/5) * valor_c + 32
    print("{:>18} {:>18.0f}".format(valor_c, valor_f))

# Exercício 3:

# Um funcionário de uma empresa recebe aumento salarial anualmente. 
# Sabe-se que: 

# a) Esse funcionário foi contratado em 2005, com salário inicial de 
# R$ 5.000,00; 

# b) Em 2006 ele recebeu aumento de 1,5% sobre o salário inicial; 

# c) A partir de 2007 (inclusive), os aumentos salariais sempre 
# corresponderam ao dobro do percentual do ano anterior. 

# Faça um programa que recebe um ano (ano > 2007) e determina o salário 
# atual do funcionário.

def ex3():
  ano = int(input("Digite o ano desejado: "))
  
  salario = 5000
  aumento_salarial = 0.015

  if ano > 2007:
    for i in range(2006, ano+1):
      salario *= (aumento_salarial + 1)
      aumento_salarial *= 2
  
  print("Salário de {0}: R$ {1:.2f}".format(ano, salario))

# Exercício 4:

# Faça um programa que leia um valor N inteiro e positivo, calcule e 
# mostre o valor de E, conforme a fórmula a seguir: 

# E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/N

def ex4():
  n = int(input("Digite o número desejado: "))

  e = 1
  for i in range(0, n):
    e += (1/(i+1))
  
  print("%.3f" % e)

# Exercício 5:

# Faça um programa que receba um número inteiro maior que 1 e verifique 
# se o número fornecido é primo ou não. Mostre uma mensagem de número primo 
# ou de número não primo. Um número é primo quando é divisível apenas pelo 
# número um e por ele mesmo.

def ex5():
  numero = int(input("Digite o número desejado: "))

  for i in range(2, numero):
    if numero % i == 0:
      print('Número não primo')
      break
  else:
    print('Número primo')

# Exercício 6:

# O Máximo Divisor Comum (MDC) de dois números inteiros positivos, 
# n e m, é o maior número, d, que divide de forma inteira n e m. 
# Existem vários algoritmos que podem ser usados para resolver esse 
# problema, incluindo: 

# Inicialize d para ser o menor número entre m e n.
# Enquanto d não dividir m e n de forma inteira faça
#   Diminua o valor de d em 1
# Relate d como o maior divisor comum de n e m

# Utilize o pseudocódigo acima para fazer um programa em Python que leia 
# dois números inteiros positivos do usuário, determina e reporta o maior 
# divisor comum entre eles.

def ex6():
  n = int(input("Digite n: "))
  m = int(input("Digite m: "))

  d = min([m, n])

  while m % d != 0 or n % d != 0:
    d -= 1

  print(d)

# Exercício 7:

# Newton descobriu um método para aproximar os valores das raízes de uma 
# equação numérica. Esse método é bastante simples e é conhecido como 
# método de Newton. Escreva um programa que implemente o método de Newton 
# para calcular e exibir a raiz quadrada de um número x digitado pelo
# usuário. O algoritmo (pseudocódigo) para o método de Newton é o 
# seguinte:

# Leia x do usuario
# Inicialize a variavel palpite para ser igual a x/2
# Inicialize a variavel erro para ser igual a | palpite^2 - x |
# Enquanto erro > 10^-12 faça
#   Atualize palpite para ser igual a média entre palpite e x/palpite
#   Atualize erro para ser igual a diferença entre palpite^2 e x
# Escreva palpite

from math import *

def ex7():
  x = int(input("Digite o número desejado: "))

  palpite = x/2
  erro = abs((palpite**2) - x)

  while erro > (10**-12):
    palpite = (palpite + (x/palpite)) / 2
    erro = (palpite ** 2) - x

  print("%.3f" % palpite)

# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()