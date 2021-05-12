def ler(name):
  arquivo = open(name, "r")
  conteudo = arquivo.readlines()
  arquivo.close()

  conteudo = conteudo[1::]
  return conteudo


def retiraClasseTamanho(lista):
  newList = []
  for linha in lista:
    if 'ball' in linha:
      newList.append(linha)

  lista = newList
  newList = []
  for linha in lista:
    newLinha = []
    palavras = linha.split(',')
    newLinha.append(palavras[0]+","+palavras[3]+","+palavras[4]+","+palavras[5]+","+palavras[6]+","+palavras[7])
    newList.append(newLinha)
  
  return newList