# Exercício 9:

# Desafio: Faça um programa que crie uma lista com vinte números 
# inteiros aleatórios (de 0 a 200). Ordene, então, essa lista de 
# forma crescente

import random as rdn

def main():
  l = []
  for i in range(20):
    l.append(rdn.randint(0, 200))
    
  l.sort()
  print(l)

main()