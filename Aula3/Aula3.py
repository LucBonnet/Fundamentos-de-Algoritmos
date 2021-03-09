# SAÍDA DE DADOS

# Função print()

print("Olá Mundo!!!")

a = 4
print(a)

a = 3
print("a vale", a)

## Composição

# -> Combinar várias strings com o valor de variáveis
anos = 30
print("João tem %d anos" % anos)

# O simbolo %d é chamado de marcador 
# marcador indoca que naquela posição estaremos colocando o valor da variável anos, que deve ser um número inteiro, neste exemplo

# --> %d - Número inteiro (int)
# --> %f - Números decimais (float)
# --> %s - Strings

#Exemplos:
a = "Olá"
dia = 4
mes = 3
print("%s hoje é dia %d do mês %d" % (a, dia, mes))

pi = 3.141592
print("O PI vale: %f" % pi)

# limitando a quantidade de casas decimais na impressão
# -> basta incluir .x entre o % e o f, onde x é o número desejado de casas decimais
#Ex:
print("O PI vale %.2f" % pi)

## Format

# -> formata a string dada de acordo com o desejado para saída de dados
# Ex:
nome = "Fulano"
peso = 78.51
# 1:2.1f -> 1 posição format / 2 casas antes da virgula ; 1 casas depois da virgula
print("O {0} pesa {1:2.1f} Kg".format(nome, peso))

# Simbolo no fluxograma 
# fluxogramaSaida.png

# Pseudocódigo

# ESCREVA "Olá Mundo!"
# ou
# WRITE "Olá Mundo!"




# ENTRADA DE DADOS

# Função input()

# -> A entrada de dados é feita pela função input()
# -> input() aceita como parâmetro um mensagem a ser exibida
# -> O valor recebido pela entrada de dados deve ser atribuído a uma variável
# -> Todo valor recebido pela função input() tem sempre o tipo string
# -> Se a ideia é utilizar o valor recebido em alguma conta ou cálculo, ele deve se convertido para algum tipo numérico

# Ex: 
pi = float(input("Digite o valor de pi: "))
print("O valor digitado é %.1f" % pi)

# Simbolo no fluxograma 
# fluxogramaEntrada.png

# Pseudocódigo

# LEIA valor1
# ou
# READ valor1 



# OPERADORES ARITMÉTICOS

# +  -> Soma
# -  -> Subtração
# /  -> Divisão
# // -> Divisão Exata
# %  -> Módulo: resto da divisão
# ** -> Potência: x ** y




# FUNÇÕES MATEMÁTICAS

# * É necessário importar o módulo de matemática
# from math import *

# -> abs(x)      -> Valor absoluto de x |x|
# -> sqrt(x)     -> Raiz quadrada de x
# -> log(x)      -> Logaritmo natural de x
# -> log10(x)    -> Lofaritmo base 10 de x
# -> sin(x)      -> Seno de x em radianos
# -> cos(x)      -> Cosseno de x em radianos
# -> exp(x)      -> e ** x
# -> round(x, n) -> Número x arredondado para n dígitos



# OPERADORES RELACIONAIS

# -> Operadores relacionais são utilizados para se realizar comparações entre valores;
# -> Estes valores podem ou não estar armazenados em variáveis
# -> O resultado de toda comparação é um tipo lógico: True ou False

# == -> Igualdade      -> =
# >  -> Maior que      -> >
# <  -> Menor que      -> <
# != -> Diferente      -> ≠
# >= -> Maior ou igual -> ≥
# <= -> Menor ou igual -> ≤

print(5 > 9)
print(9 == 9)
print(7 > 3)
print(4 != 6)
print(2 >= 2)

a = 10
b = -5

print(b >= a)
print(b <= a)
print(b != a)
print(b == a)


# ESTRUTURA CONDICIONAL

# -> Nem sempre todas as linhas do código devem ser executadas
# -> Normalmente, o programa deve decidir quais partes serão executadas com base em uma ou mais condições
# -> As condições são construídas com operadores relacionais: são feitas com base no resultado de comparações

# Comando if

# if <condição>:
#   bloco verdadeiro

def exemplo1():
  a = int(input("Primeiro valor: "))
  b = int(input("Segundo valor: "))

  if a > b:
    print("O primeiro valor é o maior")

  if b > a:
    print("O segundo valor é o maior")

  if b == a:
    print("Os dois valores são iguais")

# exemplo1()



# ELSE

# -> Comando else (senão) é utilizado nos casos em que a segunda condição é simplesmente o contrário da primeira
# -> Sempre utilizado como uma sequência do if
# -> if <condição>:
#      bloco verdadeiro
#    else:
#      bloco contrário