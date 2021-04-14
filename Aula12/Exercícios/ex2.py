# Exercício 2:

# Crie um programa que leia números inteiros 
# do usuário até que o número 0 seja inserido. 
# Uma vez que todos os números inteiros tenham 
# sido lidos, seu programa deve exibir todos 
# os números negativos, seguidos por todos os 
# números positivos.
# Dentro de cada grupo, os números devem ser 
# exibidos na mesma ordem em que foram inseridos 
# pelo usuário

numeros = []
num = int(input(''))
numeros.append(num)

while num != 0:
  num = int(input(''))
  numeros.append(num)

negativos = []
positivos = []
for num in numeros:
  if num < 0:
    negativos.append(num)
  else:
    positivos.append(num)

for num in negativos[::-1]:
  positivos.insert(0, num)
  
positivos.pop(len(positivos)-1)
print(positivos)

