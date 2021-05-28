from math import *

print("------------ Projeto Calculo I ------------")
print('Nomes e RAs:')
print("")
print("Jean-Luc Bonnet  RA: 22121108-9")
print("Enzo fávaro      RA: 22121110-5")
print("Victor Alexandre RA:22121122-0")
print('')
print("-------------------------------------------")

# Entrar com valor de w
w = complex(input("Digite w: "))
# Entrar com valor de M
m = int(input("Digite M: "))

# Pede um M novo sempre que o M digitado for menor ou igual a 0
while m <= 0:
  print("M deve ser um valor inteiro maior ou igual a 0")
  m = int(input("Digite M: "))

# Entrar com e
e = float(input("Digite ε: "))

# Pede um e novo sempre que o e digitado for menor ou igual a 0
while e <= 0:
  print("ε deve ser um valor real maior ou igual a 0")
  e = int(input("Digite ε: "))

# Define z a partir de n
def z(n):
  # Se n = 0 retorna 0
  if n == 0:
    return 0
  return (z(n-1))**2 + w

# def y(n):
#   return 1/n

x = []
for i in range(m+1):
  linha = []
  for j in range(m):
    if j >= i:
      valor = 0
    else: 
      valor = abs(z(i+1) - z(j+1))
    valor = "{0:.4f}".format(valor)
    linha.append(float(valor))
  x.append(linha)
x.pop(0)

print(*x, sep="\n")

k = []

# vetor com os valores de distância menores que e
valores_menores_e = []
for i in range(m-1):
  valores_menores_e = []
  print('coluna:', i)
  for j in range(len(x)-1):
    v = x[j][i]
    print(j, '->', v)
    if v < e:
      valores_menores_e.append(v)
  print('----------')
  i +=1
  print("{:0.4f}".format(1.4235116073289224e+127))
  print(1.4235116073289224e+127 < 3)
  print(1.4235 < 3)
  if len(valores_menores_e) == (m-1):
    k.append(i) 


#printa o resultado
if len(k) == 0:
	#se nao exitir indice menor que e
  print('Não há índice a partir do qual um elemento e seus subsequentes estejam a uma distância menor que', e)
else:
	#menor indice de k
  print('O menor índice procurado é:', min(k))
