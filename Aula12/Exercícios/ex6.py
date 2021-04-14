# Exercício 6:

# Escreva uma função que recebe 
# uma lista de números inteiros e 
# retorne uma nova lista que contém 
# o quadrado de cada um desses 
# números. Você só precisa entregar o 
# código da função.

def quadrado(l):
  new_l = []
  for n in l:
    new_l.append(n**2)
  return new_l

print(quadrado([1, 2, 3, 4, 5, 6, 7]))
