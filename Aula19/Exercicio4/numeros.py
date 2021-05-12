def crivo(lim):
  numeros = []
  for i in range(2, lim + 1):
    numeros.append(i)

  p = 2

  while p < lim:
    for i in range(0, len(numeros)):
      if numeros[i] % p == 0 and not numeros[i] == p:
        numeros[i] = 0
    p += 1   

  numeros.insert(0, 0)
  numeros.insert(0, 0)

  return numeros




