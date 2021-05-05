# Exercício 4:

# Crie uma função chamada spellChecker() que recebe 
# uma String e verifica se as palavras dessa String 
# estão corretas, para verificação utilize o arquivo 
# words.txt (o arquivo possui 466k palavras), que 
# possuí todas as palavras do inglês. Sua função 
# deverá retornar uma listas das palavras que não 
# forem encontradas no arquivo.0

def spellChecker(frase):
  file = open('words.txt', 'r')
  palavras = file.readlines()
  palavras = ' '.join(palavras).strip().lower().replace('\n', '').split(' ')
  file.close()

  frase = frase.lower()
  frase = frase.replace(',', '')
  frase = frase.split(' ')

  erradas = []
  for palavra in frase:
    if palavra not in palavras:
      erradas.append(palavra)
  return erradas
    
print(spellChecker("Automation engineers are experts who have the knowledge and ability to design, create, develop and manage systems"))