# Ex 1

# Neste exercício, você criará um programa que lê uma letra 
# do alfabeto. Se o usuário digitar a, e, i, o ou u, seu 
# programa deverá exibir uma mensagem indicando que a letra 
# inserida é uma vogal. Se o usuário digitar y, seu 
# programa deve exibir uma mensagem indicando que às 
# vezes y é uma vogal (depende da língua, no inglês, por 
# exemplo), e às vezes y é uma consoante. Caso contrário, 
# seu programa deve exibir uma mensagem indicando que a 
# letra é uma consoante.

def ex1():
  letra = input("Digite a letra desejada: ")

  vogais = ['a', 'e', 'i', 'o', 'u']

  if letra in vogais:
    print('Essa letra é uma vogal')
  elif letra == 'y':
    print('Essa letra, em algumas línguas, pode ser considerada como uma vogal e, em outras, como uma consoante.')
  else:
    print('Essa letra é uma consoante.')

# Ex 2

# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2+bx+c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário as seguintes situações:

# 1. Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
# 2. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
# 3. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# 4. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# Utilize sempre 3 casas decimais nas respostas.

from math import *

def ex2():
  a = float(input("Digite o valor de a: "))
  if a == 0:
    print("Essa equação não é do segundo grau!")
  else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - (4*a*c)

    if delta < 0:
      print("Não existem raizes reais!")
    elif delta == 0:
      r1 = (-(b)) / (2 * a)
      print(f"Raiz: {r1:.3f}")
    else:
      r1 = (-(b) + sqrt(delta)) / (2 * a)
      r2 = (-(b) - sqrt(delta)) / (2 * a)
      print("Primeira raiz: %.3f" % r1)
      print("Segunda raiz: %.3f" % r2)

# Ex 3

# Escreva um programa que determine o nome de uma forma pelo seu número de lados. O programa deve ler o número de lados que o usuário digitar e, em seguida, informar o nome apropriado. Seu programa deve suportar formas com 3 até (e incluindo) 10 lados. Se um número de lados fora desse intervalo for inserido então seu programa deve exibir uma mensagem de erro apropriada.

def ex3():
  n_lados = int(input("Digite o número de lados desejados: "))

  if n_lados < 3:
    print("O programa não suporta a quantidade informada")
  if n_lados == 3:
    print("Triângulo.")
  if n_lados == 4:
    print("Quadrilátero.")
  if n_lados == 5:
    print("Pentágono.")
  if n_lados == 6:
    print("Hexágono.")
  if n_lados == 7:
    print("Heptágono.")
  if n_lados == 8:
    print("Octágono.")
  if n_lados == 9:
    print("Eneágono.")
  if n_lados == 10:
    print("Decágono.")
  if n_lados > 10:
    print("O programa não suporta a quantidade informada")

# Ex 4

# O ano é dividido em quatro estações: primavera, verão, outono e inverno. As datas exatas em que as estações mudam podem variar um pouco de ano para ano por causa da maneira que o calendário é construído. Neste exercício, usaremos as seguintes datas limites:

# Estação	Primeiro Dia
# Outono    |  20 de Março                        
# Inverno	  |  21 de Junho
# Primavera	|  22 de Setembro
# Verão	    |  21 de Dezembro

# Crie um programa que recebe do usuário um mês e um dia. O usuário entrará o nome do mês como uma string, seguido do dia do mês como um inteiro. Então, seu programa deve exibir a estação associada à data que foi introduzida.

def ex4():
  dia = int(input("Digite o dia desejado: "))
  mes = input("Digite o mês desejado: ")

  if dia >= 20 and mes == 'março' or mes in ['abril', 'maio'] or dia < 21 and mes == 'junho':
    print('Outono')
  elif dia >= 21 and mes == 'junho' or mes in ['julho', 'agosto'] or dia < 22 and mes == 'setembro':
    print('Inverno')
  elif dia >= 22 and mes == 'setembro' or mes in ['outubro', 'novembro'] or dia < 21 and mes == 'dezembro':
    print('Primavera')
  elif dia >= 21 and mes == 'dezembro' or mes in ['janeiro', 'fevereiro'] or dia < 20 and mes == 'março':
    print('Verão')
    
# Ex 5

# Em uma universidade particular, as notas são mapeadas para pontos da seguinte maneira:

# Nota |  Pontos               
# A+	 |  5.0
# A	   |  5.0
# A-	 |  4.5
# B+	 |  4.0
# B	   |  3.5
# B-	 |  3.0
# C+	 |  2.5
# C 	 |  2.0
# C-	 |  1.5
# D+	 |  1.0
# D	   |  0.5
# F	   |  0.0

# Escreva um programa que comece lendo uma nota (em letra) do usuário. Então, o seu programa deve computar e exibir o número equivalente de pontos. Certifique-se de que seu programa gere uma mensagem de erro apropriada se o usuário inserir uma nota inválida.

def ex5():
  nota = input("Digite a nota em letra, e o sinal +/-: ")

  if nota == 'A+':
    print("{0} é equivalente a 5.0".format(nota))
  elif nota == 'A':
    print("{0} é equivalente a 5.0".format(nota))
  elif nota == 'A-':
    print("{0} é equivalente a 4.5".format(nota))
  elif nota == 'B+':
    print("{0} é equivalente a 4.0".format(nota))
  elif nota == 'B':
    print("{0} é equivalente a 3.5".format(nota))
  elif nota == 'B-':
    print("{0} é equivalente a 3.0".format(nota))
  elif nota == 'C+':
    print("{0} é equivalente a 2.5".format(nota))
  elif nota == 'C':
    print("{0} é equivalente a 2.0".format(nota))
  elif nota == 'C-':
    print("{0} é equivalente a 1.5".format(nota))
  elif nota == 'D+':
    print("{0} é equivalente a 1.0".format(nota))
  elif nota == 'D':
    print("{0} é equivalente a 0.5".format(nota))
  elif nota == 'F':
    print("{0} é equivalente a 0.0".format(nota))
  else:
    print("Nota inválida")

# Ex 6

# Posições em um tabuleiro de xadrez são identificadas por uma letra e um número. As letras identificam as colunas, enquanto os números identificam as linhas, conforme mostrado abaixo:

# Escreva um programa que leia uma posição inserida por um usuário. Primeiro a coluna, depois a linha. Então, seu programa deve informar qual é a cor do quadrado relacionado à posição digitada.
# Para isso, utilize uma declaração if para determinar se a coluna começa com um quadrado preto ou um quadrado branco. Em seguida, use modular aritmética (%) para relatar a cor do quadrado nessa linha. Por exemplo, se o usuário entrar a - 1 então seu programa deve informar que o quadrado é preto. Se o usuário digitar d - 5 então seu programa deve informar que o quadrado é branco. Seu programa pode assumir que uma posição válida sempre será inserida.

def ex6():
  linha = int(input("Digite a linha desejada: "))
  coluna = input("Digite a coluna desejada: ")

  cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

  coluna = cols.index(coluna) + 1

  casa = 0

  if coluna % 2 == 0:
    casa = 0  
    if linha % 2 == 0:
      casa = 1
  else: 
    casa = 1
    if linha % 2 == 0:
      casa = 0

  if casa == 0:
    print('Branco')
  else:
    print('Preto')  

# Ex 7

# O zodíaco chinês atribui animais a anos em um ciclo de 12 anos. Um ciclo de 12 anos é mostrado na tabela abaixo. O padrão se repete a partir daí, com 2012 sendo outro ano do Dragão, e 1999 sendo mais um ano da Lebre.

# Ano   | Animal    
# 2000	| Dragão
# 2001	| Cobra
# 2002	| Cavalo
# 2003	| Carneiro
# 2004	| Macaco
# 2005	| Galo
# 2006	| Cachorro
# 2007	| Porco
# 2008	| Rato
# 2009	| Boi
# 2010	| Tigre
# 2011	| Lebre

# Escreva um programa que leia um ano do usuário e exiba o animal associado com aquele ano. Seu programa deve funcionar corretamente para qualquer ano maior ou igual a zero, não apenas para os listados na tabela acima.
# Dica: Podemos reconhecer padrões cíclicos com o operador % (resto da divisão).

def ex7():
  ano = int(input("Digite um ano: "))

  modulo = ano % 12
  animal = ''

  if modulo == 8:
    animal = 'Dragão'
  elif modulo == 9: 
    animal = 'Cobra'
  elif modulo == 10:
    animal = 'Cavalo'
  elif modulo == 11:
    animal = 'Carneiro'
  elif modulo == 0:
    animal= 'Macaco'
  elif modulo == 1:
    animal= 'Galo'
  elif modulo == 2:
    animal= 'Cachorro'
  elif modulo == 3:
    animal= 'Porco'
  elif modulo == 4:
    animal= 'Rato'
  elif modulo == 5:
    animal= 'Boi'
  elif modulo == 6:
    animal= 'Tigre'
  elif modulo == 7:
    animal= 'Lebre'

  print("{0} é o ano do(a) {1}".format(ano, animal))

# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()