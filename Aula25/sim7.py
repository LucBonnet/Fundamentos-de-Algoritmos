n = int(input())

lista = [0, 1]
for i in range(2, n):
  lista.append(lista[i-1] + lista[i-2])

print(*lista)