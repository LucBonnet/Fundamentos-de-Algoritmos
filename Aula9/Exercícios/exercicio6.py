# Exercício 6:

# Escreva uma função que calcula o quociente e o resto da 
# divisão inteira entre dois números. Utilize apenas as 
# operações de soma e subtração para calcular o resultado. 
# Dica: utilize uma estrutura de repetição para isso.
# Faça um programa principal que recebe o dividendo e o 
# divisor do usuário e, depois de chamar a função, exibe o 
# quociente e o resto.

def quocienteResto(dividendo, divisor):
  vezes = 0

  while dividendo >= divisor:
    vezes += divisor
    dividendo = dividendo - divisor

  print("Quociente: ", vezes)
  print("Resto: ", dividendo)
    
# quocienteResto(25, 3)

dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

quocienteResto(dividendo, divisor)
