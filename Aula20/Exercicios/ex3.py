# Exercício 3:

# Crie uma função que retorna o número de 
# caracteres únicos em uma string criada 
# pelo usuário. Por exemplo, Hello, World! 
# tem 10 caracteres únicos, enquanto zzz 
# tem somente 1 caractere único. Use um 
# dicionário para resolver este problema.

def caracteresUnicos(string):
  dic = {}
  for letra in string:
    if letra in dic:
      dic[letra] += 1
    else:
      dic[letra] = 1
  
  qtd = 0
  for chave, valor in dic.items():
    qtd += 1

  return qtd

def main():
  frase = input("Digite a string desejada: ")
  qtd = caracteresUnicos(frase)

  print(qtd)

main()