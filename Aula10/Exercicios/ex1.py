# Exercício 1

# Escreva uma função que tenha os comprimentos dos dois lados mais 
# curtos de um triângulo retângulo como seus parâmetros. Retorne a 
# hipotenusa do triângulo, calculada usando o teorema de Pitágoras,
# como o resultado da função. Inclua um programa principal que lê os 
# comprimentos dos lados mais curtos de um triângulo retângulo do usuário 
# e use sua função para calcular o comprimento da hipotenusa. Exiba o 
# resultado.

from math import *

# Calcula a hipotenusa a partir de 2 catetos
def hip(c1, c2):
  hip = sqrt(c1**2 + c2**2)
  return hip

def main():
  cateto1 = float(input("Digite o primeiro lado do triângulo: "))
  cateto2 = float(input("Digite o segundo lado do triângulo: "))

  hipotenusa = hip(cateto1, cateto2)

  print('Hipotenusa: %.2f' % hipotenusa)

main()
  