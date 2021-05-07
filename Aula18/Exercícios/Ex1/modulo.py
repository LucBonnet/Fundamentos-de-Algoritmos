def doaSangue(sexo, peso):
  if sexo == 'm':
    return peso >= 60
  elif sexo == 'f':
    return peso >= 50
  else:
    print('sexo: m/f')