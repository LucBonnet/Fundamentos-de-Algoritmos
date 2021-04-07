# Exercício 4:

# Uma data é considerada mágica quando o dia multiplicado pelo 
# mês é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 
# 1960 é uma data mágica porque junho é o sexto mês e 6 vezes 
# 10 é 60, o que equivale ao ano de dois dígitos. Escreva uma 
# função que determine se uma data é ou não uma data mágica. 
# Use sua função em um programa que deve encontrar e exibir 
# todas as datas mágicas do século XX.

def dataMagica(dia, mes, ano):
  ano = str(ano)
  if len(ano) > 2:
    ano = int(ano) % 100

  return dia * mes == ano

# print(dataMagica(10, 6, 1960))

# Datas mágicas do século XX (1, 1, 1901) - (31, 12, 2000):

from datetime import *

# Soma um dia a uma data especifica
# data = date(1901, 1, 1)
# print(data)
# data = data + timedelta(days = 1)

# print(data)

def main():
  dataInicial = date(1901, 1, 1)
  dataFinal = date(2000, 12, 31)

  data = dataInicial

  while data != dataFinal:
    data = data + timedelta(days = 1)
    isMagic = dataMagica(data.day, data.month, data.year)

    if isMagic:
      print("{0}/{1}/{2}".format(data.day, data.month, data.year))

main()