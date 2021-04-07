# Exercício 1:

# Escreva uma função com parâmetros que retorne o maior de 
# dois números. A função deve se chamar maximo(x, y).

def maximo(x, y):
  if x > y:
    return x
  else:
    return y

print(maximo(1, 2))
print(maximo(5, 3))
print(maximo(20, 2))
print(maximo(3, 8))
print(maximo(-9, -1))
