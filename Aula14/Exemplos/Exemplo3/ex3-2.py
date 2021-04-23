# Leitura de dois dados na mesma linha

contatos = open("contatos.dat", "r")
conteudo = contatos.readlines()

print(conteudo)

contato = []

for linha in conteudo:
  linha_separada = linha.split(" ")
  linha_separada[len(linha_separada)-1] = linha_separada[len(linha_separada)-1].strip()
  contato.append(linha_separada)

print(contato)