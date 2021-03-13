# Estruturas Condicionais Continuação

# Exemplo:
def exemplo1():
  distancia = float(input("Qual a distância você pretende percorrer (km): "))

  if distancia <= 200:
    preco = 0.5 * distancia
  else:
    preco = 0.45 * distancia

  print(f"O preço da passagem será: {preco:.2f}")

# exemplo1()

# Condições aninhadas

# -> Muitas vezes é preciso aninhar vários ifs para obter o comportamento 
# desejado
# -> Aninhar significa colocar um if dentro do outro (ou um if dentro do else).

# Exemplo:
def exemplo2():
  minutos = int(input("Quantos minutos foram utilizados este mês: "))

  if minutos > 400:
    preco = 0.15
  else:
    if minutos < 200:
      preco = 0.2
    else:
      preco = 0.18

  print("O valor da sua conta é R$ %.2f" % (minutos*preco))

# exemplo2()

# Exemplo:
def exemplo3():
  n1 = float(input("Digite o valor da primeira nota: "))
  n2 = float(input("Digite o valor da segunda nota: "))

  m = (n1 + n2) / 2

  if m >= 5:
    if m == 10:
      print("Aprovado com Distinção")
    else: 
      print("Aprovado")
  else:
    print("Reprovado")

# exemplo3()

# Comando elif

# -> O comando elif(else if - senão se) substitui, em muitos casos, a 
# necessidade do aninhamento
# -> é sempre utilizado como uma sequência de um if

# Exemplo:
def exemplo4():
  minutos = int(input("Quantos minutos foram utilizados este mês: "))

  if minutos < 200:
    preco = 0.2
  elif minutos < 400:
    preco = 0.18
  else:
    preco = 0.15
  
  print("O valor da sua conta é R$ %.2f" % (minutos*preco))

# print(5<7<10) --> True
# exemplo4()

# Exemplo:
def exemplo5():
  num1 = float(input("Digite um número: "))
  num2 = float(input("Digite outro número: "))

  op = input("Digite a operação desejada: ")

  if op == '+':
    print(f"{num1} {op} {num2} = {num1 + num2}")
  elif op == '-':
    print(f"{num1} {op} {num2} = {num1 - num2}")
  elif op == '*':
    print(f"{num1} {op} {num2} = {num1 * num2}")
  elif op == '/':
    print(f"{num1} {op} {num2} = {num1 / num2}")
  elif op == '**':
    print(f"{num1} {op} {num2} = {num1 ** num2}")
  elif op == '//':
    print(f"{num1} {op} {num2} = {num1 // num2}")
  elif op == '%':
    print(f"{num1} {op} {num2} = {num1 % num2}")
  else:
    print("Operador não identificado")

# exemplo5()

# Fluxograma:
# imgs/fluxogramaCondição.png

# Pseudocódigo

# SE (a < b) ENTÃO
#   Comandos para condição verdadeira
# SENÃO
#   Comandos caso contrário

# ou

# IF (a < b) THEN
#   Comandos para condição verdadeira
# ELSE
#   Comandos caso contrário

# Exemplo de Fluxograma
# imgs/fluxogramaExemplo.png

# Pseudocódigo do exemplo

# INÍCIO
#   ESCREVA "Digite o primeiro dígito: "
#   LEIA a
#   ESCREVA "Digite o segundo número: "
#   LEIA b
#   SE (a < b) ENTÃO 
#     ESCREVA "O segundo dígito é maior"
#   SENÃO
#     ESCREVA "O primeiro dígito é maior"
#   FIM-SE
# FIM

# Comentários

# -> São textos que não são interpretados como código de programa
# -> Servem para documentar o programa
# -> Começa com o símbolo '#'

# Operadores Lógicos

# -> Podemos combinar condições para determinar como continuar o fluxo de um programa
# -> O Python fornece operadores lógicos para permitir a construção de condições
# mais complexas.
# -> Os operadores lógicos são:
#    * and  (E condicional)
#    * or  (OU condicional)
#    * not     (NÃO lógico)
# -> Sempre retornam um valor Booleano: True ou False

# AND

# Comparação 1 | Comparação 2 | Resultado 
# True         | True         | True
# True         | False        | False
# False        | True         | False
# False        | False        | False

# OR

# Comparação 1 | Comparação 2 | Resultado 
# True         | True         | True
# True         | False        | True
# False        | True         | True
# False        | False        | False

# NOT

# Comparação | Resultado
# True       | False
# False      | True

# Exemplo:

# Faça um programa que lê um ano como entrada e verifica se esse ano é bissexto.
def exemplo6():
  ano = int(input("Digite um ano: "))

  if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print("Bissexto!")
  else:
    print("Não Bissexto!")

# exemplo6()

# Precedência de Operadores

# ^  | **                                   | Exponencial
# |  | *, @, /, //, %                       | Multiplicação, multiplicação de matrizes, divisão, resto
# |  | +, -                                 | Adição e Subtração
# |  | in, is, is not, <, <=, >, >=, !=, == | Comparações
# |  | not x                                | NÃO booleano 
# |  | and                                  | E booleano
# |  | or                                   | OU booleano
# |  | if - elif - else                     | Expressões condicionais

# Exemplo:
def exemplo7():
  x = 3
  y = 4

  if 4 + x < y + 6 or x - 7 > 10 + y / 2 and x**3 >= 10:
    #4 + 3 < 4 + 6 or 3 - 7 > 10 + 4 / 2 and 3**3 >= 10
    #4 + 3 < 4 + 6 or 3 - 7 > 10 + 4 / 2 and 9 >= 10
    #4 + 3 < 4 + 6 or 3 - 7 > 10 + 2 and 9 >= 10
    #7 < 10 or -4 > 12 and 9 >= 10
    #True or False and False
    #True or False
    #True
    print("Sim")
  else:
    print("Não")

# exemplo7()

# Exercicio 1:

# Leia 2 valores reais (x e y), que devem representar as coordenadas de um 
# ponto em um plano. Então, determine a que quadrante (Q1, Q2, Q3 ou Q4) o 
# ponto pertence ou se está sobre um dos eixos cartesianos ou na origem (x = 
# y = 0).

def exercicio1():
  x = float(input("X: "))
  y = float(input("Y: "))

  if x == 0 and y == 0 :
    print("O ponto está na origem")
  elif y == 0:
    print("O ponto pertence ao eixo da coordenadas")
  elif x == 0:
    print("O ponto pertence ao eixo das abississas")
  
  if x > 0 and y > 0:
    print("O ponto pertence ao Quadrante 1")
  elif x < 0 and y > 0:
    print("O ponto pertence ao Quadrante 2")
  elif x < 0 and y < 0:
    print("O ponto pertence ao Quadrante 3")
  elif x > 0 and y < 0:
    print("O ponto pertence ao Quadrante 4")
    
# exercicio1()

# Exercício 2:

# A empresa X resolveu conceder um aumento de salários a seus funcionários 
# de acordo com a tabela abaixo:

#     Salário       | Percentual
#   0 - 400.00      |    15%
#  400.01 - 800.00  |    12%
#  800.01 - 1200.00 |    10%
# 1200.01 - 2000.00 |     7%
#  Acima de 2000.00 |     4%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o 
# valor de reajuste ganho e o índice reajustado, em percentual.

def exercicio2():
  salario = float(input("Digite o salário: "))

  if salario == 0 and salario <= 400:
    indice_de_reajuste = 15
    novo_salario = salario * 1.15
    valor_do_reajuste = salario * 0.15
  elif salario >= 400.01 and salario <= 800:
    indice_de_reajuste = 12
    novo_salario = salario * 1.12
    valor_do_reajuste = salario * 0.12
  elif salario >= 800.01 and salario <= 1200:
    indice_de_reajuste = 10
    novo_salario = salario * 1.10
    valor_do_reajuste = salario * 0.10
  elif salario >= 1200.01 and salario <= 2000:
    indice_de_reajuste = 7
    novo_salario = salario * 1.07
    valor_do_reajuste = salario * 0.07
  elif salario > 2000:
    indice_de_reajuste = 4
    novo_salario = salario * 1.04
    valor_do_reajuste = salario * 0.04
  
  print(f"Novo salário: R${novo_salario:.2f}")
  print(f"Valor de reajuste ganho: R${valor_do_reajuste:.2f}")
  print(f"índice de reajuste: {indice_de_reajuste:.2f}%")

# exercicio2()

# Exercício 3:

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# ● “Telefonou para a vítima?”
# ● “Esteve no local do crime?”
# ● ‘Mora perto da vítima?”
# ● “Devia para a vítima?”
# ● “Já trabalhou com a vítima?” 
# Então, o programa deve emitir uma classificação sobre a participação da 
# pessoa no crime. Se a pessoa responder positivamente a 2 questões, ela 
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
# "Assassino". Caso contrário, ele será classificado como "Inocente".

def exercicio3():
  resp = ['', '', '', '', '']

  resp[0] = input("Telefonou para a vítima?\n")
  resp[1] = input("Esteve no local do crime?\n")
  resp[2] = input("Mora perto da vítima?\n")
  resp[3] = input("Devia para a vítima?\n")
  resp[4] = input("Já trabalhou com a vítima?\n")

  cont = 0

  for resposta in resp :
    resposta = resposta.lower()
    if resposta == 'sim':
      cont += 1
  
  if cont < 2:
    print("Inocente")  
  elif cont == 2:
    print("Suspeita")
  elif cont <= 4:
    print("Cúmplice")
  elif cont >= 5:
    print("Assassino")

# exercicio3()

# Exercício 4:

# Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax^2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer 
# as consistências, informando ao usuário as seguintes situações:

# a. Se o usuário informar o valor de a igual a zero, a equação não é do 
# segundo grau e o programa não deve pedir os demais valores, sendo 
# encerrado;

# b. Se o delta calculado for negativo, a equação não possui raízes reais. 
# Informe ao usuário e encerre o programa;

# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz 
# real; informe-a ao usuário;

# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao 
# usuário;

from math import *

def exercicio4():
  a = float(input("a: "))
  if a == 0:
    print("Esta equação não é do segundo grau")
    return
  b = float(input("b: "))
  c = float(input("c: "))

  delta = b**2 - (4*a*c)

  if delta < 0:
    print("A equação não possui raízes reais")
  elif delta == 0:
    r1 = (-(b)) / (2 * a)
    print(f"A equação possui apenas uma raiz: {r1}")
  else:
    r1 = (-(b) + sqrt(delta)) / (2 * a)
    r2 = (-(b) - sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raízes reais: {r1} e {r2}")

# exercicio4()

# Exercício 5:

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# a. Álcool:
#   i.  até 20 litros, desconto de 3% por litro
#   ii. acima de 20 litros, desconto de 5% por litro
# b. Gasolina:
#   i.  até 20 litros, desconto de 4% por litro
#   ii. acima de 20 litros, desconto de 6% por litro 

# Escreva um programa que solicita o número de litros vendidos e o tipo de 
# combustível (álcool ou gasolina). Então, calcule e imprima o valor a ser pago 
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,00 e, do 
# álcool, R$ 2,40.

def exercicio5():
  litros = float(input("Digite a quantidade de litros vendida: "))
  comb = input("Digite o tipo de combustível: ")

  preco_gas = 4.00
  preco_alcool = 2.40

  if comb == 'álcool' or comb == 'alcool':
    if litros <= 20:
      desconto = 0.03
    else:
      desconto = 0.05

    preco = (litros * preco_alcool) - (litros * preco_alcool) * desconto
  elif comb == 'gasolina':
    if litros <= 20:
      desconto = 0.04
    else:
      desconto = 0.06
    
    preco = (litros * preco_gas) - (litros * preco_gas) * desconto
  else:
    print("Combustível não encontrado")
  
  print(f"Valor a ser pago R${preco}")
  
# exercicio5()

# Exercício 6:

# Faça um programa para um caixa eletrônico. O programa deverá perguntar 
# ao usuário o valor do saque e depois informar quantas notas de cada valor 
# serão fornecidas. O programa sempre tenta dar a menor quantidade de notas 
# possível. As notas disponíveis são as de 1, 5, 10, 50 e 100 reais. O valor 
# mínimo de saque é de 10 reais e o máximo de 1000 reais. O programa não 
# deve se preocupar com a quantidade de notas existentes na máquina.

# a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
# notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e 
# quatro notas de 1.

def exercicio6():
  saque = float(input("Valor do saque: "))

  if saque < 10 or saque > 1000:
    print("Valor inválido")
  
  n_cem = int(saque // 100)
  saque = saque % 100
  n_cinquenta = int(saque // 50)
  saque = saque % 50
  n_dez = int(saque // 10)
  saque = saque % 10
  n_cinco = int(saque // 5)
  saque = saque % 5
  n_um = int(saque)

  print(f"{n_cem} notas de 100 reais")
  print(f"{n_cinquenta} notas de 50 reais")
  print(f"{n_dez} notas de 10 reais")
  print(f"{n_cinco} notas de 5 reais")
  print(f"{n_um} notas de 1 real")

exercicio6()