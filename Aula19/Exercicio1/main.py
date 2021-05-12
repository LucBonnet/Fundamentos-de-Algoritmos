# Exercicio 1:

# Crie um módulo com 3 funções que, juntas, servirão 
# para a criação de placas de veículos no novo padrão 
# do Mercosul. O novo padrão é composto por quatro 
# letras e três números: AAA0A00

# Assim, sua primeira função deve gerar 4 letras 
# aleatoriamente, a segunda função deve gerar 3 números 
# inteiros aleatoriamente e a terceira função deve 
# juntar as letras e os números no padrão correto: 
# letra-letra-letra-num-letra num-num (AAA0A00).

# Escreva um programa principal que chama as três funções 
# e exibe a placa criada.

from placas import letrasRdn, numerosRdn, geraPlaca

import random
random.seed(100)

def main():
  numeros = numerosRdn()
  letras = letrasRdn()
  placa = geraPlaca(letras, numeros)

  print("Placa =", placa)

if __name__ == "__main__":
  main()
