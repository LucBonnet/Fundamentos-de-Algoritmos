def ordenar(string):
  palavras = string.split('-')
  palavras = sorted(palavras)
  palavras = '-'.join(palavras)

  return palavras

def contar(string):
  maiusculas = 0
  minusculas = 0

  for letra in string:
    if letra.islower():
      minusculas += 1
    elif letra.isupper():
      maiusculas += 1
  
  return [maiusculas, minusculas]