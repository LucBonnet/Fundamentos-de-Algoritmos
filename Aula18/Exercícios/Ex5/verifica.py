def isInteger(valor):
  if len(valor) < 1:
    return False
  
  if valor[0] in ['+', '-']:
    if valor[1::].isnumeric():
      return True
    else:
      return False
  
  if valor.isnumeric():
    return True
  else:
    return False