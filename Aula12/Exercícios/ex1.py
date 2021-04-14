# Exercício 1:

# Faça um programa que leia uma a um modelos de cinco 
# carros (exemplos: FUSCA, GOL, VECTRA etc) e os guarde em uma 
# mesma lista. Leia (um a um) uma outra lista  com o consumo 
# desses carros, isto é, quantos quilômetros cada um desses carros 
# faz com um litro de combustível. Calcule e mostre:
# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros 
# cadastrados consome para percorrer uma distância de 
# 1000 quilômetros.

carros = []
for i in range(5):
  carros.append(input(''))

consumo = []
indice = 0
for i in range(5):
  cons = float(input(''))
  if cons > consumo[indice]:
    economico = cons
    indice = i
  consumo.append(cons)

print(carros[indice])

for con in consumo:
  print('%.0f' % (1000/con))
