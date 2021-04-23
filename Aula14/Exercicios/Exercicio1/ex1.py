# Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A 
# primeira linha deve conter o maior número e a última linha o menor. Salve o 
# resultado em outro arquivo, chamado pares_invertido.txt.

pares = open("pares.txt", "r")
pares_invertido = open("pares_invertido.txt", "w")

conteudo = pares.readlines()
pares.close()
conteudo = conteudo[::-1]

for i in conteudo:
  pares_invertido.write(i)

pares_invertido.close()
