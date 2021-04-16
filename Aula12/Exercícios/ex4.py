# Exercício 4:

# Faça um Programa que leia 20 números inteiros e 
# armazene-os em uma lista. 
# Armazene os números pares na lista par e os 
# números ímpares na lista impar. 
# Imprima as três listas no final.

numeros = []
par = []
impar = []
for i in range(20):
  num = int(input(''))
  numeros.append(str(num))
  if num % 2 == 0:
    par.append(str(num))
  else:
    impar.append(str(num))

print(*numeros)
print(*impar)
print(*par)
