# Exercício 5:

# Faça uma função que receba quatro valores: I, A, B e C. 
# Destes Valores, I é um valor inteiro valendo 1, 2 ou 3. 
# A, B e C são valores reais. Escreva os números A, B e C 
# obedecendo à tabela a seguir, dependendo do valor de I

# Valor de I | Forma a Escrever                          |
# 1          | A, B e C em ordem crescente               |
# 2          | A, B e C em ordem decrescente             |
# 3          | O maior fica entre os outros dois números |

def ordemValores(i, a, b, c):
  numeros = [a, b, c]
  if i == 1:
    numeros = sorted(numeros)
    print(', '.join(str(num) for num in numeros))
  elif i == 2:
    numeros = sorted(numeros, reverse=True)
    print(', '.join(str(num) for num in numeros))
  elif i == 3:
    numeros = sorted(numeros)
    print('{0}, {1}, {2}'.format(numeros[0], numeros[2], numeros[1]))
  else:
    print('Valor inváildo de i')

ordemValores(1, 1, 2, 3)
ordemValores(2, 1, 2, 3)
ordemValores(3, 1, 2, 3)
ordemValores(4, 1, 2, 3)