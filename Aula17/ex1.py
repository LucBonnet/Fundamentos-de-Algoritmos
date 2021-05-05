# Exercício 1

# Crie uma função em Python chamada contaPalavras 
# que recebe uma string e conta quantas palavras 
# tem nessa string. Sua função deve  retornar o 
# número de palavras contadas. 

def contaPalavras(frase):
  palavras = frase.split(' ')
  return len(palavras)

  
print(contaPalavras("A FEI eh fantastica"))