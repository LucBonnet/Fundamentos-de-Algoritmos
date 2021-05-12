# Exercício 4:

# O crivo de Eratóstenes é uma técnica 
# que foi desenvolvida há mais de 2.000 
# anos atrás para encontrar facilmente 
# todos os números primos entre 2 e 
# algum limite. Uma descrição 
# (pseudocódigo) do algoritmo é a 
# seguinte:

# Este algoritmo está baseado no fato de 
# ser relativamente fácil desconsiderar 
# todos os números n em um pedaço de 
# papel. Essa também é uma tarefa fácil 
# para um computador - um loop for pode 
# simular esse comportamento quando um 
# terceiro parâmetro (step) é fornecido 
# para a função rangeovo. Quando um 
# número é descartado, sabemos que ele 
# não é mais primo, mas ainda ocupa 
# espaço no pedaço de papel, e ainda deve 
# ser considerado ao computar números 
# primos posteriores.

# Como resultado, você não deve 
# descartar um número removendo-o da 
# lista. Em vez disso, você deve descartar 
# um número substituindo-o por 0. Em 
# seguida, assim que o algoritmo for 
# concluído, todos os valores diferentes 
# de zero na lista serão primos. Crie um 
# módulo em Python com uma função que 
# implementa o crivo de Eratóstenes para 
# salvar todos os números primos entre 2 
# e um limite dado em uma lista. No 
# programa principal, receba o número 
# inteiro que será o limite da verificação 
# de primos e exiba todos os números 
# encontrados. Se tudo estiver correto, 
# a sua função deve ser capaz de retornar 
# a lista com todos os números primos 
# menores que 1.000.000, por exemplo, em 
# apenas alguns segundos.

from numeros import crivo

def main():
  limite = int(input("Digite um limite para os números primos: "))
  lista = crivo(limite)

  print(*lista)

if __name__ == "__main__":
  main()