def capitalLetter(frase):
  n = []
  for caracter in frase:
    n.append(caracter)
  n[0] = n[0].upper()
  for i in range(len(n)):
    if n[i] in ['!', '.', '?']:
      if i+2 <= len(n):
        n[i+2] = n[i+2].upper()
        
  return ''.join(n)