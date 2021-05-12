import random

def letrasRdn():
  letrasEx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  letras = []
  for i in range(4):
    letra = random.choice(letrasEx)
    letras.append(letra)
  return letras

def numerosRdn():
  numeros = []
  for i in range(3):
    num = str(random.randrange(9))
    numeros.append(num)
  return numeros

def geraPlaca(letras, numeros):
  placa = letras[0] + letras[1] + letras[2]
  placa += numeros[0]
  placa += letras[3]
  placa += numeros[1] + numeros[2]

  return placa
