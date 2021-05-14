# Exercício 4:

# Duas palavras são anagramas se contiverem 
# todas as mesmas letras, mas em uma ordem 
# diferente. Por exemplo, estante e setenta 
# são anagramas. Crie uma função que recebe 
# duas strings do usuário e determina se elas 
# são ou não anagramas. Utilize dicionário 
# para resolver o problema.

def isAnagrama(string1, string2):
  dic1 = {}
  for letra in string1: 
    if letra in dic1:
      dic1[letra] += 1
    else:
      dic1[letra] = 1
  
  dic2 = {}
  for letra in string2: 
    if letra in dic2:
      dic2[letra] += 1
    else:
      dic2[letra] = 1

  return dic1 == dic2

def main():
  p1 = input("Digite a primeira palavra: ")
  p2 = input("Digite a segunda palavra: ")

  resp = isAnagrama(p1, p2)

  if resp:
    print('Essa palavras são anagramas')
  else:
    print('Essa palavras não são anagramas')

main()