file = open("Python.txt", "r", encoding='utf8')
palavras = file.readlines()
file.close()
palavras = " ".join(palavras)
palavras = palavras.replace(",", "").replace(".", "")
palavras = palavras.split()

maior = 0
maioresPalavras = []
for palavra in palavras:
  palavra = palavra.strip()
  if len(palavra) > maior:
    maior = len(palavra)
    maioresPalavras = []
  if len(palavra) == maior:
    maioresPalavras.append(palavra)

print(maioresPalavras)