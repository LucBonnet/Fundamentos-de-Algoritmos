# Exercício 2:

# Crie uma função em Python chamada contaPalavras 
# que recebe uma string e que conte a quantidade 
# de incidências de todas as palavras em uma string, 
# assim listando todas as palavras e suas 
# quantidades. Sua função deve  retornar o número 
# de palavras contadas  em formato de dicionário.

# A função deverá retornar um dicionário referente 
# as palavras encontradas (sem duplicidade) e a 
# quantidade de incidência de cada uma das palavras.

# Sua função deverá considerar todas as palavras 
# como letras minúsculas, remova também as virgulas 
# e os caracteres "!" e "?".

# Obs: Utilize dicionário para solucionar o 
# problema, conforme apresentado em aula.

def contaPalavras(text):
  text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').strip()
  text = text.lower()
  dic = {}
  palavras = text.split(' ')
  for palavra in palavras:
    if palavra in dic:
      dic[palavra] += 1
    else:
      dic[palavra] = 1

  return dic

frase = "Um teste, dois testes, mais testes, acabou?, SIM !!!"
print(contaPalavras(frase))