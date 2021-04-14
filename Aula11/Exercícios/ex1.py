# Exercício 1:

# Crie um programa em que peça 10 números reais, armazene-os em uma 
# lista e diga qual é o índice do maior, e seu valor.

def main():
  l = []
  for i in range(10):
    num = float(input("Digite um valor real: "))
    l.append(num)
  
  maior = l[0]
  i = 0
  for index in range(len(l)):
    if l[index] > maior:
      maior = l[index]
      i = index

  print('O maior valor é %f e está no índice %d' % (maior, i))

main()