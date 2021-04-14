# Exercício 6:

# As temperaturas de uma cidade foram armazenadas na lista 
# temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4 ]. Faça um programa 
# que imprime a menor e a maior temperatura, assim como a média.

def main():
  temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4 ]

  menor = temperaturas[0]
  maior = temperaturas[0]
  soma = 0

  for item in temperaturas:
    if item < menor:
      menor = item
    if item > maior:
      maior = item
    
    soma += item
  
  media = soma/len(temperaturas)
  print('Menor valor:', menor)
  print('Maior valor:', maior)
  print('Méida:', media)
  
main()