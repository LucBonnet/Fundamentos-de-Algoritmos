# Exercício 3

# Crie uma função chamada produtorio que realize o cálculo do 
# produtório, conforme equação abaixo:

# Π xi = xm * xm+1 * xm+2 * ... * xn-1

# Sua função deverá receber entre 3 e 6 parâmetros e retornar o 
# valor do produtório. Não é necessário fazer o programa 
# principal.

# Produtório é a multiplicação de uma sequência de objetos
# matemáticos (números, funções, vetores, matrizes, etc.).

# Calcula o produtorio entre 3 e 6 valores
def produtorio(n1, n2, n3, n4=1, n5=1, n6=1):
  return n1 * n2 * n3 * n4 * n5 * n6

## ou (função que recebe infinitos valores)

def prod(*args):
  result = 1
  for num in args:
    result *= num
  return result

print(produt(2, 2, 2, 2))