arquivo = open("teste.txt", "w")

for i in range(100):
  arquivo.write("%d\n" % i)

arquivo.close()