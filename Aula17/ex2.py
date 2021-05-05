# Exercício 2:

# A Criptografia de César é uma técnica bastante 
# Trata-se de um tipo de substituição, na qual cada 
# letra de um texto a ser criptografado é substituída 
# por outra letra presente no alfabeto, porém 
# deslocada um certo número de posições à esquerda 
# ou à direita.

# Por exemplo, se empregarmos uma troca de quatro 
# posições à esquerda, cada letra é substituída pela 
# letra que está quatro posições adiante no alfabeto, 
# e nesse caso a letra A seria substituída pela letra 
# E, a letra B por F, a letra C por G, e assim 
# sucessivamente.

# Crie uma função chamada criptCesar que recebe 
# uma frase e o valor do deslocamento, podendo ser 
# positivo ou negativo. A criptografia deverá ser 
# cíclica, como na imagem acima; isso significa que 
# quando terminar em Z o próximo caractere é A.

# Sua função deve ignorar caracteres minúsculos, 
# especiais e os espaços.simples e provavelmente a 
# mais conhecida de todas.

# Trata-se de um tipo de substituição, na qual cada 
# letra de um texto a ser criptografado é substituída 
# por outra letra presente no alfabeto, porém deslocada 
# um certo número de posições à esquerda ou à direita.

# Por exemplo, se empregarmos uma troca de quatro posições 
# à esquerda, cada letra é substituída pela letra que está 
# quatro posições adiante no alfabeto, e nesse caso a 
# letra A seria substituída pela letra E, a letra B por 
# F, a letra C por G, e assim sucessivamente.

# Crie uma função chamada criptCesar que recebe uma frase 
# e o valor do deslocamento, podendo ser positivo ou 
# negativo. A criptografia deverá ser cíclica, como na 
# imagem acima; isso significa que quando terminar em Z 
# o próximo caractere é A.

# Sua função deve ignorar caracteres minúsculos, 
# especiais e os espaços.

def criptCesar(frase, num):
  letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  frase = frase.upper()

  encript = ''
  for i in range(len(frase)):
    letra = frase[i]
    if letra in letras:
      index = letras.index(letra)
      encript += letras[(index+num) % len(letras)]
    else:
      encript += letra
  print(encript)

p = "SURJUDPDQGR HP SBWKRQ !!!"
criptCesar(p, -3)