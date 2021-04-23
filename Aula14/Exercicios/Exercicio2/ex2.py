# Escreva uma função em Python para retornar a somatória de todos os 
# números que estão armazenados no arquivo “numeros2.txt”. Todos os 
# números do arquivo estão na mesma e única linha, separados por espaço.

def somatoria():
  arquivo = open("numeros2.txt", "r")

  conteudo = arquivo.readlines()
  conteudo = conteudo[0].split(" ")
  
  soma = 0
  for i in conteudo:
    soma += int(i)
  print("Soma:", soma)

somatoria()