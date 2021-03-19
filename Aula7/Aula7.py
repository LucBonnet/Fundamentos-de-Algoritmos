# Estruturas de repetição

# Repetições

# -> São utilizadas para executar várias vezes a mesma parte do programa
# -> Normalmente dependem de uma condição
# -> Repetições são a base de vários programas!

# While

# -> O comando while (enquanto) serve para executarmos alguma repetição 
# enquanto uma condição for verdadeira (True)

# Exemplo 1:

def exemplo1():
  x = 1
  while x <= 10:
    print(x)
    x += 1

# exemplo1()

# Exercício 1:

# Escreva um programa que faça a contagem regressiva de 10 até 0. O 
# programa deve imprimir cada número da contagem a cada um segundo.

from time import sleep

def exercicio1():
  x = 10
  while x >= 0:
    print(x)
    # subtrai 1 do valor de x
    x -= 1
    # pausa o código por x segundos
    sleep(1)

# exercicio1()

# Exemplo 2:

# Impressão do número 1 até o número digitado pelo usuário

def exemplo2():
  ultimo = int(input("Digite o último dígito da contagem: "))
  i = 1
  while i <= ultimo:
    print(i)
    i += 1

# exemplo2()

# Exemplo 3: Combinando repetição com if

# Programa que imprime todos os números pares de 0 até um número 
# digitado pelo usuário.

def exemplo3():
  ultimo = int(input("Digite o último dígito da contagem: "))

  i = 0
  while i <= ultimo:
    if i % 2 == 0:
      print(i)
    i += 1

# exemplo3()

# Exercício 2:

# Escreva um programa que imprime a tabuada do número digitado pelo 
# usuário.

def exercicio2():
  numero = int(input("Digite o número dejesado: "))

  i = 0
  while i <= 10:
    print("{0} x {1} = {2}".format(numero, i, numero * i))
    i += 1

# exercicio2()

# Exercíco 3:

# Faça um programa que solicita um número entre 0 e 10. Mostre uma 
# mensagem de erro caso o valor seja inválido e continue pedindo até que o 
# usuário informe um valor válido. Quando o valor for válido dê a mensagem 
# “número aceito!”

def exercicio3():
  x = -1
  while not (x >= 0 and x <= 10):
    print('Valor inválido')
    x = int(input("Digite um número entre 0 e 10: "))
  print('Número aceito!')

# exercicio3()

# Exemplo 4:

# Programa para calcular a somatória de 10 números que devem ser digitados 
# pelo usuário.

def exemplo4():
  n = 1
  soma = 0

  while n <= 10:
    x = float(input("Digite o %d° número: " % n))
    soma = soma + x
    n += 1
  print("Soma", soma)

# exemplo4()

# While infinito

# -> Muitas vezes, queremos que nossos programas sejam executados infinitamente
# -> Nesses casos, podemos utilizar uma condição que nunca deixe de ser verdadeira (True)

# while True:
# # bloco a ser executado

# Comando break

# -> Porém, mesmo quando utilizamos um while infinito, é possível que em determinadas situações o 
# programa precise sair do loop de repetição 
# -> Esta interrupção pode ser alcançada com o comando break
# -> O comando break pode ser utilizado para interromper o while, 
# independente da condição

# Exemplo:

# Somatória de valores digitados pelo usuário até que o número 0 (zero) seja 
# digitado; quando 0 for digitado o resultado da somatória é exibido:

def exemplo5():
  somatoria = 0

  while True:
    entrada = int(input("Digite um número a somar ou 0 para sair: "))
    if entrada == 0:
      break
    else:
      somatoria += entrada

  print("Somatória", somatoria)

# exemplo5()

# Repetições aninhadas

# -> Podemos combinar vários while, um dentro do outro!
# -> Com isso, conseguimos alterar automaticamente o valor de mais do 
# que somente uma variável

# Exemplo 6:

# Programa para calcular as tabuadas do número 1 até o número 10.

def exemplo6():
  tabuada = 1

  while tabuada <= 10:
    print("\nTabuada do", tabuada)
    
    multiplicador = 0
    while multiplicador <= 10:
      print("{0} x {1} = {2}".format(tabuada, multiplicador, (tabuada*multiplicador)))
      multiplicador += 1
    
    tabuada += 1

# exemplo6()

# For

# -> for é a estrutura de repetição mais utilizada 
# -> sintaxe: for <referencia> in <sequencia>
# -> durante a execução, a cada interação, a referência aponta para um elemento 
# da sequência
# -> Uma vantagem do for com relação ao while é que o contador não precisa
# ser explícito!

# Exemplo 7:

# Calcular a somatória dos números de 0 a 99

def exemplo7():
  somatoria = 0

  # a função range(i, f, p) é bastante utilizada nos laços com for
  # ela gera um conjunto de valores inteiros
  # * Começando em i
  # * Até valores menores de f
  # * Com passo p
  # Se o passo p não for definido, seu padrão será 1
  for x in range(0, 100):
    somatoria += x
  print(somatoria)

# exemplo7()

# Exercício 4:

# Faça um programa que gera 100 vezes um número aleatório entre 1 e 100 e, 
# então, exiba qual foi o maior número gerado e quantas vezes o maior número 
# foi atualizado no seu código. 
# Para isso, você deve comparar o número gerado na iteração presente com o 
# maior número armazenado até o momento.

from random import randrange

def exercicio4():
  vezes = 0
  maior_numero = 0
  for i in range(0, 100):
    num = randrange(1, 101)
    if num > maior_numero:
      vezes += 1
      maior_numero = num
  print("Maior número gerado:", maior_numero)
  print("Vezes que foi atualizado:", vezes)

# exercicio4()

# Comando else na repetição

# -> É possível a utilização do comando else nas estruturas de repetição
# -> Tanto no while quanto no for
# -> A cláusula else só é executada quando a condição do loop se torna falsa
# -> Se você sair do loop com o comando break, por exemplo, ela não será executada

# Exemplo 8:

def exemplo8():
  i = 0
  while i < 11:
    print(i)
    i += 2
  else:
    print("Os números pares de 0 a 10 foram exibidos")

# exemplo8()

# Exemplo 9:

def exemplo9():
  for i in range(0, 11, 2):
    print(i)
  else:
    print("Os números pares de 0 a 10 foram exibidos")

# exemplo9()

# Exemplo 10: exemplo com break

def exemplo10():
  i = 0

  while i < 11:
    print(i)
    i += 2
    if i == 8: 
      break
  else:
    print("Os números pares de 0 a 10 foram exibidos")

# exemplo10()

# Comando continue na repetição

# -> O comando contiunue funciona de maneira parecida com o break, porém 
# o break interrompe e sai do loop
# -> Já o continue faz com que a próxima iteração comece a ser executada, não
# importando se existem mais comandos depois dele ou não
# -> O continue não sai do loop
# -> O continue faz com que a próxima iteração seja executada imediatamente

# Exemplo 11:

def exemplo11():
  i = 0
  while i < 12:
    i += 2
    if i == 8:
      continue
    print(i)
  else:
    print("Os números pares de 2 a 12 foram exibidos, com exceção do 8")

# exemplo11()

# Fluxograma de repetição:

# img/fluxogramaRepeticao.png

# Pseudocódigo:

# ENQUANTO (a < b) FAÇA
#   Comandos para condição verdadeira
# FIM-ENQUANTO

# ou

# WHILE (a < b) DO
#   Comandos para condição verdadeira
# END-WHILE

# Exemplo de Fluxograma:

# img/fluxogramaExemplo.png

# Exemplo de Pseudocódigo

# INÍCIO
#   contador = 1
#   ENQUANTO (contador < 100) FAÇA
#     ESCREVA contador
#     contador = contador + 1
#   ENQUANTO-FIM
# FIM

# Exercício 5:

# Escreva um programa que calcula a média aritmética de 5 números digitados 
# pelo usuário. Utilize contadores e acumuladores.

def exercicio5():
  soma = 0
  for i in range(0, 5):
    n = float(input("Digite o %d° valor: " % (i + 1)))
    soma += n
  media = soma / 5
  print('Média:', media)

# exercicio5()

# Exercício 6:

# Escreva um programa que leia números digitados pelo usuário. O programa 
# deve ler os números até que 0 (zero) seja digitado. Quando 0 for digitado, o 
# programa deve exibir a quantidade de dígitos que foram digitados, a 
# somatória destes dígitos e a média aritmética.

def exercicio6():
  vezes = 0
  soma = 0
  x = -1
  while x != 0:
    x = float(input("Digite um valor: "))
    if x != 0:
      vezes += 1
      soma += x
  else:
    print("Foram digitados %d números" % vezes)
    print("Somatória:", soma)
    print("Média aritmética:", (soma/vezes))

# exercicio6()

# Exercício 7:

# Um zoológico em particular determina o preço da entrada com base na idade 
# do visitante. Os visitantes com 2 anos de idade ou menos têm entrada 
# gratuita. Crianças entre 3 e 12 anos pagam R$ 14,00. Idosos com 65 anos ou 
# mais pagam R$ 18,00. A entrada para todos os outros visitantes custa R$ 
# 23,00. 

# Crie um programa que comece lendo as idades de todos os visitantes de um 
# mesmo grupo, sendo uma idade informada em cada linha. O usuário digitará 
# uma linha em branco para indicar que não há mais pessoas no grupo. Em 
# seguida, seu programa deve exibir o custo total para o grupo. O custo deve 
# ser exibido usando duas casas decimais.

def exercicio7():
  idade = 0
  valor = 0
  while idade != '':
    idade = input("")
    if idade != '':
      idade = int(idade)
      if idade <= 2:
        valor += 0
      elif idade >= 3 and idade <= 12:
        valor += 14
      elif idade >= 65: 
        valor += 18
      else:
        valor += 23
  print('Custo total %.2f' % valor)

# exercicio7()

# Exercício 8:

# Escreva um programa que calcule o perímetro de um polígono. Comece recebendo do usuário os 
# valores de x e y para o primeiro ponto do polígono. Em seguida, continue lendo pares de valores x 
# e y até que o usuário insira uma linha em branco para a coordenada x. Cada vez que você lê uma 
# coordenada adicional, você deve calcular a distância até o ponto anterior e adicioná-la ao 
# perímetro. Quando uma linha em branco for inserida para a coordenada x, seu programa deve 
# adicionar a distância do último ponto de volta ao primeiro ponto. Em seguida, ele deve exibir o 
# perímetro total. Um exemplo de entrada e saída é mostrado abaixo, com a entrada do usuário em 
# negrito:

# Digite o x da coordenada: 0
# Digite o y da coordenada: 0
# Digite o x da coordenada (em branco para sair): 1
# Digite o y da coordenada: 0
# Digite o x da coordenada (em branco para sair): 0
# Digite o y da coordenada: 1
# Digite o x da coordenada (em branco para sair):

# O perímetro desse polígono é 3.414213562373095

from math import *

def exercicio8():
  x1 = int(input("Digite o x da coordenada: "))
  y1 = int(input("Digite o y da coordenada: "))
  x = 0
  x0 = x1
  y0 = y1
  p = 0
  while x != '':
    x = input("Digite o x da coordenada (em branco para sair): ")
    if x != '':
      y = int(input("Digite o y da coordenada: "))
      x = int(x)
      dx = abs(x0 - x)
      dy = abs(y0 - y)
      d = abs(sqrt(dx**2 + dy**2))
      p += d
      x0 = x
      y0 = y
    else: 
      dx = abs(x0 - x1)
      dy = abs(y0 - y1)
      d = abs(sqrt(dx**2 + dy**2))
      p += d
  print(p)

exercicio8()
