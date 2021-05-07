# Exercício 5:

# Você deve criar um módulo composto por uma 
# função chamada isInteger que determina se 
# os caracteres em uma string representam ou 
# não um inteiro válido. Uma string representa 
# um inteiro se seu comprimento for pelo menos 
# igual a 1 e contiver apenas dígitos, ou se 
# seu primeiro caractere for + ou - seguido por 
# um ou mais caracteres, todos os quais devem 
# ser dígitos. Escreva um programa principal 
# que lê uma string do usuário e informa se 
# ela representa ou não um inteiro por meio da 
# função criada. 

from verifica import isInteger

def main():
  num = input("Digite um número: ")

  if isInteger(num):
    print("O número é inteiro")
  else: 
    print("O número não é inteiro")

if __name__ == "__main__":
  main()
