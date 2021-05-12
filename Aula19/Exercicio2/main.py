# Exercício 2:

# Escreva um módulo em Python com uma 
# função que recebe uma string com as 
# palavras separadas por hífen. A 
# função deverá ordenar as palavras 
# mantendo-as separadas por hífen; 
# escreva uma segunda função que recebe 
# essa string e calcula a quantidade de 
# letras maiúsculas e minúsculas. 
# Escreva também um programa principal 
# (função main) para testar as funções.

from verStrings import contar, ordenar

def main():
  string = input("Digite as palavras desejadas separando-as por hífen(-): ")
  print(ordenar(string))

  num = contar(string)
  print("Maiúsculas =", num[0])
  print("Minúsculas =", num[1])

if __name__ == "__main__":
  main()