# Exercício 1:

# Faça uma função chamada converte() que recebe um dicionário 
# (dicionário criado pelo Moodle, sempre com o nome codigo_morse) 
# e uma String contendo uma frase e retorne uma frase convertida em 
# código Morse.

# Sua função deverá traduzir cada letra e número para o código Morse, 
# deixando um espaço entre cada letra ou número. Sua função deverá 
# ignorar qualquer caractere que não seja letra ou número.

# O dicionário referente ao código Morse de cada letra e número será 
# fornecido conforme tabela abaixo:

codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}

def converte(cod, text):
  text = text.upper()
  newText = []
  for letter in text:
    if letter in cod:
      newText.append(cod[letter])
  
  newText = ' '.join(newText)

  return newText

print(converte(codigo_morse, "Hello World!!!"))