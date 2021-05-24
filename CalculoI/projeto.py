from math import *

print('Nomes e RAs')

w = complex(input("Digite w: "))
m = int(input("Digite M: "))

while m < 0:
  print("M deve ser um valor inteiro maior ou igual a 0")
  m = int(input("Digite M: "))

e = float(input("Digite ε: "))

while e < 0:
  print("ε deve ser um valor real maior ou igual a 0")
  e = int(input("Digite ε: "))

def z(n):
  if n == 0:
    return 0
  return (z(n-1))**2 + w

def y(n):
  return 1/n

k = 0

x = []
for i in range(m-1):
  linha = []
  for j in range(m-1):
    if j == i:
      continue
    if j == i + 1:
      break

    valor = abs(y(i+1) - y(j+1))
    print(valor, e)
    linha.append(round(valor, 4))
  x.append(linha)
x.pop(0)

print(x)
print(k)