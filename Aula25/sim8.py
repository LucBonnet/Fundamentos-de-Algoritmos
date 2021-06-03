n = int(input("Digite o valor de N:"))

x=[]
for i in range(n):
  v = int(input("Digite o " + str(i+1) + " valor de X:"))
  x.append(v)

menor = x[0]
index = 0
for i in range(n):
  if x[i] < menor:
    menor = x[i]
    index = i

print("Menor valor:", menor)
print("Posicao:", index)