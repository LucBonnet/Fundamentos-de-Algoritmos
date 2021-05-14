# Exercicio 2:

# Neste exercício, você simulará 1.000 lançamentos 
# de dois dados. Comece escrevendo uma função que 
# simula o lançamento de um par de dados de seis 
# lados cada. Sua função não deve aceitar nenhum 
# parâmetro. Ela retornará a somatória obtida 
# pelos dois dados. Escreva um programa principal 
# que use sua função para simular 1.000 lançamentos 
# de dois dados. Como acontece em alguns programas, 
# você deve contar o número de vezes que cada 
# somatória acontece. Em seguida, a função 
# principal deve exibir uma tabela que resume 
# esses resultados. Mostre a frequência para cada
# resultado como uma porcentagem do número total 
# de lançamentos.

import random as rdn

def doisDados():
  num1 = rdn.randint(1, 6)
  num2 = rdn.randint(1, 6)

  return num1 + num2

def main():
  dic = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
  }

  vezes = 1000000
  for i in range(vezes):
    soma = doisDados()
    dic[soma] += 1
  
  for chave, valor in dic.items():
    print("%3d = %3d: %f%%" % (chave, valor, (valor*100)/vezes))

main()

