file = open("Python.txt", "r", encoding="utf8")
palavras = file.readlines()
file.close()
palavras = " ".join(palavras).lower()
palavras = palavras.replace(",", "").replace(".", "")
palavras = palavras.split()

palavrasMaisFreq = []
maisFreq = 0
for palavra in palavras:
  palavra = palavra.strip()
  contador = palavras.count(palavra)
  if contador > maisFreq:
    maisFreq = contador
    palavrasMaisFreq = []
  if contador == maisFreq and not palavra in palavrasMaisFreq:
    palavrasMaisFreq.append(palavra)
  
print(palavrasMaisFreq)