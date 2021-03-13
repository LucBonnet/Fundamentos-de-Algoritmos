# Ex 1:
def ex1():
  faixa_etaria = input("Digite a faixa etária: ")

  msg = ""
  if faixa_etaria == 'Bebê':
    msg = 'menor que 2 anos'
  if faixa_etaria == 'Criança':
    msg = 'de 3 a 10 anos'
  if faixa_etaria == 'Adolescente':
    msg = 'de 11 a 17 anos'
  if faixa_etaria == 'Adulto':
    msg = 'de 18 a 64 anos'
  if faixa_etaria == 'Idoso':
    msg = 'maior que 65 anos'

  print(msg)
  
# Ex 2:
def ex2():
  p1 = float(input("Digite o valor do primeiro produto: "))
  p2 = float(input("Digite o valor do segundo produto: "))
  p3 = float(input("Digite o valor do terceiro produto: "))

  tot = p1 + p2 + p3

  desconto = 0

  if tot > 500:
    desconto = tot * (20/100)
  else:
    desconto = tot * (10/100)

  print("Desconto: %.2f" % desconto)  

# Ex 3:
def ex3():
  n_lados = int(input(""))

  if n_lados < 3:
    print("Erro!")
  if n_lados == 3:
    print("triângulo")
  if n_lados == 4:
    print("quadrado")
  if n_lados == 5:
    print("pentágono")
  if n_lados == 6:
    print("hexágono")
  if n_lados == 7:
    print("heptágono")
  if n_lados == 8:
    print("octógono")
  if n_lados == 9:
    print("eneágono")
  if n_lados == 10:
    print("decágono")
  if n_lados > 10:
    print("Erro!")

# Ex 4
def ex4():
  valor = float(input("Digite o valor da compra: "))
  parcelas = int(input("Digite a quantidade de parcelas: "))

  desconto1 = 0.00
  desconto2 = 0.00

  if valor > 5000:
    desconto1 = valor * (5/100)
  if valor <= 5000:
    desconto1 = 0

  if parcelas == 1:
    desconto2 = valor * (10/100)
  if parcelas == 2 or parcelas == 3:
    desconto2 = valor * (5/100)
  if parcelas > 3:
    desconto2 = 0

  tot_desconto = desconto1 + desconto2

  print("Desconto total: %.2f" % tot_desconto)
  print("Valor final da compra com desconto: %.2f" % (valor - tot_desconto))
  print("Cada parcela será de: %.2f" % ((valor - tot_desconto) / parcelas))

from math import *

# Ex 5:
def ex5():
  pol = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ")
  aresta = float(input("Digite o valor da aresta a em metros: "))

  v = 0

  if pol == "dodecaedro":
    v = ((15 + sqrt(5) * 7) / 4) * (aresta ** 3)
  if pol == "icosaedro":
    v = (5 / 12) * (3 + sqrt(5)) * (aresta ** 3)

  print("O volume de um {0} regular com {1:.2f} de aresta é: {2:.2f}".format(pol, aresta, v))

# Ex 6:
def ex6():
  mes = input("")

  if mes == "janeiro":
    print("31 dias")
  if mes == "fevereiro":
    print("28 ou 29 dias")
  if mes == "março":
    print("31 dias")
  if mes == "abril":
    print("30 dias")
  if mes == "maio":
    print("31 dias")
  if mes == "junho":
    print("30 dias")
  if mes == "julho":
    print("31 dias")
  if mes == "agosto":
    print("31 dias")
  if mes == "setembro":
    print("30 dias")
  if mes == "outubro":
    print("31 dias")
  if mes == "novembro":
    print("30 dias")
  if mes == "dezembro":
    print("31 dias")

# Ex 7:
def ex7():
  v_bomba = float(input("Digite a vazão da bomba em l/s: "))
  capacidade = float(input("Digite a capacidade do reservatório: "))

  tempo_s = capacidade / v_bomba

  h = tempo_s // 3600
  tempo_s = tempo_s % 3600
  m = tempo_s // 60
  tempo_s = tempo_s % 60
  s = tempo_s

  print("Tempo necessário para encher o reservatório: {0:.0f}:{1:.0f}:{2:.0f}".format(h,m,s))

# Ex 8:
def ex8():
  m = float(input("Digite a medida do ovo: "))
  if m < 30:
    print("pequeno")
  else:
    print("grande")

ex8()