# Exercício 3:

# Muitas pessoas não usam letras maiúsculas 
# corretamente, especialmente ao digitar em 
# pequenos dispositivos como smartphones. Neste 
# exercício, você escreverá um módulo composto 
# por uma função que capitaliza os caracteres 
# apropriados em uma string. O primeiro caractere 
# da string deve ser sempre capitalizado, assim 
# como o primeiro caractere após “.”, “!” ou “?”.

from letters import capitalLetter

def main():
  frase = input("Digite a frase:\n")
  print(capitalLetter(frase))

if __name__ == "__main__":
  main()