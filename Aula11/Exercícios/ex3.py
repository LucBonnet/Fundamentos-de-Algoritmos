# Exercício 3:

# Faça um programa para criar uma lista de 10 elementos (pedir para o 
# usuário) e apresentar: a soma dos ELEMENTOS pares e a soma dos 
# elementos de ÍNDICE par

def main():
  l = []

  for i in range(10):
    l.append(float(input("Digite um número: ")))

  soma_elem_par = 0
  soma_indice_par = 0

  for indice in range(len(l)):
    if l[indice] % 2 == 0:
      soma_elem_par += l[indice]
    if indice % 2 == 0:
      soma_indice_par += l[indice]
  
  print('Soma dos Elementos pares: %f' % soma_elem_par)
  print('Soma dos Elementos de índice par: %f' % soma_indice_par)


main()
