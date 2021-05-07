# Exercício 2:

# Escreva um módulo que contenha uma função que 
# receba os comprimentos dos dois lados mais 
# curtos de um triângulo retângulo (catetos) como 
# seus parâmetros. A função deve retornar a 
# hipotenusa do triângulo, calculada usando o 
# teorema de Pitágoras. 
# Escreva também o programa principal que recebe 
# do usuário os comprimentos dos catetos do 
# triângulo retângulo, chama a função para 
# calcular a hipotenusa e exibe o resultado.

from modulo import hip

def main():
  cat1 = float(input("Digite o valor do primeiro cateto: "))
  cat2 = float(input("Digite o valor do segundo cateto: "))

  print("A valor da hipotenusa é", hip(cat1, cat2))

if __name__ == "__main__":
  main()