# Exercício 1:

# Crie 4 listas:
# ● Inteiros: a primeira lista com 10 números inteiros gerados 
# aleatoriamente
# ● Reais: a segunda lista com 15 números reais gerados aleatoriamente
# ● Strings: A terceira lista com 7 strings criadas por você
# ● Complexos: A quarta lista com 5 números complexos criados por você.
# Então, adicione as 4 listas a uma lista única, chamada completa. Apague 
# todas as 4 listas originais. Acesse e mostre todos os elementos da lista 
# completa. Acrescente mais 50 números inteiros gerados aleatoriamente na 
# lista de inteiros que está dentro da lista completa. 

import random as rdn

inteiros = []
for i in range(10):
  inteiros.append(rdn.randint(0, 100))
  
reais = []
for i in range(15):
  reais.append(rdn.random() * 100)

strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

complexos = [1 + 2j, 3 - 4j, 3 + 5j, 9 - 1j, 10 + 40j]

completa = [inteiros, reais, strings, complexos]

del(inteiros)
del(reais)
del(strings)
del(complexos)

for i in range(len(completa)):
  for j in range(len(completa[i])):
    print(completa[i][j])

for i in range(50):
  completa[0].append(rdn.randint(0, 100))

print(completa)
