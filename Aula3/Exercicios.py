# EX 1:
# Faça um programa que solicita do usuário uma quantidade de dias, horas,
# minutos e segundos. Calcule e imprima o total convertido em somente
# segundos. 

def ex1():
  d = int(input("Digite o número de dias: "))
  h = int(input("Digite o número de horas: "))
  m = int(input("Digite o número de minutos: "))
  s = int(input("Digite o número de segundos: "))

  t = s + (m + (h + (d * 24)) * 60) * 60

  print("Total: %ds" % t)

# EX 2:
# Escreva um programa que pergunte a quantidade de km percorridos por um
# carro alugado, assim como a quantidade de dias pelos quais o carro foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
# e R$ 0,15 por km rodado.

def ex2():
  km = float(input("Digite o Km percorrido: "))
  dias = int(input("Digite a quantidade de dias: "))

  preco = 60 * dias + 0.15 * km

  print("Valor R$%.2f" % preco)

# EX 3:
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def ex3():
  h = float(input("Digite sua altura: "))
  peso_ideal = (72.7*h) - 58

  print("Peso ideal %.2fKg" % peso_ideal)

# EX 4:
# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para
# o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS
# c. quanto pagou ao sindicato
# d. o salário líquido

def ex4():
  valor_h = float(input("Digite o valor ganho por hora: "))
  horas_t = int(input("Digite o número de horas trabalhadas no mês: "))

  salario_tot = (valor_h * horas_t)
  valor_ir = salario_tot*(11/100)
  valor_inss = salario_tot*(8/100)
  valor_sind = salario_tot*(5/100)
  
  salario_liq = salario_tot - valor_ir - valor_inss - valor_sind

  print("+ Salário Bruto: R${0:.2f}".format(salario_tot))
  print("- IR (11%): R${0:.2f}".format(valor_ir))
  print("- INSS (8%): R${0:.2f}".format(valor_inss))
  print("- Sindicato (5%): R${0:.2f}".format(valor_sind))
  print("= Salário Líquido: R${0:.2f}".format(salario_liq))
  


from math import *

# EX 5:
# y = x^3- |ln(x)|

def ex5(x = 3):
  y = x**3 - abs(log(x))
  print(y)

# EX 6:
# y = x^2 - w^k

def ex6(x = 3, w = 3, k = 3):
  y = x**2 - w**k
  print(y)

# EX 7:

def ex7(x = 3, y = 3):
  k = (exp(2) + sqrt(x+y))/3
  print(k)

# EX 8:
def ex8(x = 3):
  y = (x**2 - log10(x) + sin(x)) / (x - cos(x)**3)
  print(y)




# EX 9:
def ex9():
  a = 4
  b = 10
  c = 5.0
  d = 1
  f = 5

  print("a==c: ", a==c)
  print("a<b:", a<b)
  print("d<b:", d<b)
  print(c!=f)
  print(a==b)
  print(c<d)
  print(b>a)
  print(c>=f)
  print(f>=c)
  print(c<=c)
  print(c<=f)


# EX 10:
# Faça um Programa que peça dois números e, então, imprima o maior deles.
def ex10():
  x = float(input("Digite um número: "))
  y = float(input("Digite outro número: "))

  if x > y :
    print("O número {0} é maior que o número {1}".format(x,y))
  if y > x :
    print("O número {0} é maior que o número {1}".format(y,x))
  if x == y :
    print("O número {0} é igual ao o número {1}".format(x,y))

# EX 11:
# Faça um Programa que peça um valor numérico e escreva na tela se o valor é
# “positivo” ou “negativo”
def ex11():
  x = int(input("Digite um número inteiro: "))

  if x < 0:
    print("O número %f é negativo" % x)
  if x > 0:
    print("O número %f é positivo" % x)
  if x == 0:
    print("O número %f é igual a 0" % x)

# EX 12:
# Faça um Programa que leia um número e exiba o dia correspondente da
# semana: 1 - Domingo, 2 - Segunda etc.
def ex12():
  d = int(input("Digite um número: "))

  if d == 1:
    print("%d - Domingo" % d)
  if d == 2:
    print("%d - Segunda" % d)
  if d == 3:
    print("%d - Terça" % d)
  if d == 4:
    print("%d - Quarta" % d)
  if d == 5:
    print("%d - Quinta" % d)
  if d == 6:
    print("%d - Sexta" % d)
  if d == 7:
    print("%d - Sábado" % d)
  if d > 7:
    print("Valor inválido" % d)
  
# EX 13:
# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento
# de 10%. Para inferiores ou iguais, de 15%. Imprima o novo salário.
def ex13():
  salario = float(input("Digite seu salário: "))

  aumento = 0
  if salario > 1250:
    aumento = salario * (10/100)
  if salario <= 1250:
    aumento = salario * (15/100)

  salario += aumento

  print("O salário será de R${0:.2f}".format(salario))

# EX 14:
# Escreva um programa que deve dizer se um carro é novo (menos que 3 anos)
# ou velho (mais ou igual a 3 anos). A idade do carro deve ser informada pelo
# usuário. 
def ex14():
  idade_carro = int(input("Digite a idade do seu carro: "))

  if idade_carro < 3:
    print("O carro é novo")
  if idade_carro >= 3:
    print("O carro é velho")

# EX 15:
# Escreva um programa que pergunte a distância que um passageiro deseja
# percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens até 200 km e R$ 0,45 para viagens mais longas
def ex15():
  d = float(input("Digite a distância a ser percorrida em Km: "))

  if d <= 200:
    preco_passagem = d * 0.5
  if d > 200:
    preco_passagem = d * 0.45

  print("Preço da passagem:", preco_passagem)

# EX 16:
# Faça um Programa para leitura de três notas parciais de um aluno. O programa
# deve calcular a média (M = (N1 + N2*2 + N3*3)/6) alcançada pelo aluno e
# apresentar:
# a. A mensagem "Aprovado", se a média for maior ou igual a 5, com a
# respectiva média alcançada;
# b. A mensagem "Reprovado", se a média for menor do que 5, com a
# respectiva média alcançada;
def ex16():
  n1 = float(input("Digite a primeira nota: "))
  n2 = float(input("Digite a segunda nota: "))
  n3 = float(input("Digite a terceira nota: "))

  media = (n1 + n2*2 + n3*3) / 6

  if media >= 5:
    print("Aprovado")
  if media < 5:
    print("Reprovado")

def ex17():
  n1 = float(input("Digite a primeira nota: "))
  n2 = float(input("Digite a segunda nota: "))
  n3 = float(input("Digite a terceira nota: "))

  media = (n1 + n2*2 + n3*3) / 6

  if media >= 5:
    print("Aprovado")
  else:
    print("Reprovado")

  print("Aprovado" if media >= 5 else "Reprovado")

ex17()