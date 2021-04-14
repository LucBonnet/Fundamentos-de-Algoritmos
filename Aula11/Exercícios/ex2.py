# Exercício 2:

# Faça um programa que imprime uma sequência de n números em ordem 
# inversa à da leitura. Utilize uma lista para isso.

def main():
  n = int(input("Digite a quantidade de elementos: "))

  l = []
  for i in range(n):
    l.insert(0, float(input('Digite um número: ')))

  print(l)

main()