# Exercício 3:

# Solicitar dados de uma matriz 4x4 e montar um vetor de 
# 4 elementos com a soma dos elementos ímpares de cada linha

m = []

for i in range(4):
  linha = []
  for j in range(4):
    linha.append(int(input('Digite um número: ')))
  m.append(linha)

v = []
soma = 0
for i in range(len(m)):
  for j in range(len(m[i])):
    if m[i][j] % 2 != 0:
      soma += m[i][j]
  v.append(soma)
  soma = 0

print(v)

