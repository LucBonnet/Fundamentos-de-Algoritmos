# Exercício 7

# Escreva uma função que recebe a latitude e a longitude 
# de dois pontos (latitude e longitude do ponto A, latitude 
# e longitude do ponto B) como valores float.  Essa função 
# deve calcular e imprimir a distância em km entre os dois 
# pontos. Utilize os métodos radians, sin, cos e acos do 
# módulo math para auxiliar nos cálculos. A distância é 
# calculada conforma equação: 

# dist=6371.01*acos(sin(latitude1)∗sin(latitude2)+cos(latitude1)∗cos(latitude2)∗cos(longitude1−longitude2))

# Faça o programa principal que recebe os valores das duas 
# latitudes e das duas longitudes e chama a função.

from math import *

def distancia(latitude1, longitude1, latitude2, longitude2):
  dist = dist=6371.01*acos(sin(latitude1)*sin(latitude2)+cos(latitude1)*cos(latitude2)*cos(longitude1-longitude2))
  return dist

def main():
  latA = float(input("Digite a latitude A: "))
  longA = float(input("Digite a longitude A: "))
  latB = float(input("Digite a latitude B: "))
  longB = float(input("Digite a longitude B: "))

  print('A distância é %.2fkm.' % distancia(radians(latA), radians(longA), radians(latB), radians(longB)))

main()
