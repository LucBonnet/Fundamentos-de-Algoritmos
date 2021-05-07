# Exercício 1:

# Existem restrições para que uma pessoa possa 
# doar sangue. Uma delas é relativa ao peso. 
# Mulheres tem que pesar no mínimo 50kg e homens 
# no mínimo 60kg. Faça um módulo que contenha 
# uma função para informar se uma pessoa está 
# ou não apta a doar sangue sabendo seu sexo e 
# seu peso. O programa principal deve ler as 
# entradas, acionar a função que retorna true ou 
# false e exibir a resposta.

from modulo import doaSangue

def main():
  sexo = input("Digite o sexo: ")
  peso = float(input("Digite o peso: "))

  if doaSangue(sexo, peso):
    print("Essa pessoa pode doar sangue")
  else:
    print("Essa pessoa não pode doar sangue")

if __name__ == "__main__":
  main()