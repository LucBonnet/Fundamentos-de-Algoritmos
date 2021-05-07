def minCaracteres(senha):
  if len(senha) >= 8:
    return True
  return False

def letraMaiuscula(senha):
  for letra in senha:
    if letra.isupper():
      return True
  return False

def letraMinuscula(senha):
  for letra in senha:
    if letra.islower():
      return True
  return False

def temNumero(senha):
  for letra in senha:
    if letra.isnumeric():
      return True
  return False