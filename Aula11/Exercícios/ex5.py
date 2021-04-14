# Exercício 5:

# Faça um programa que mostra o menor valor dentro da 
# lista T = [1, 7 ,2 ,4]

def main():
  T = [1, 7 ,2 ,4]

  menor = T[0]
  for item in T:
    if item < menor:
      menor = item

  print('Menor valor: %d' % menor)

main()