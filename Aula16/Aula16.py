# Strings

# -> Cadeias de caracteres: sequência de caracteres
# -> A representação de um caractere é dada por um número 
# inteiro, hexadecimal ou binário
# -> Esse número segue um padrão conhecido entre diversos 
# sistemas computacionais:
# # -> ASCII 
# # -> UTF

# Tabela ASCII

# -> 7 bits (números de 0 a 127)

# Tabela ASCII Estendida:

# -> 8 bits
# -> Igual a abela ASCII, porém contém mais caracteres

# UTF

# -> Um dos padrões mais utilizados da atualidade é o UTF-8 
# (8-bit Unicode Transformation Format)
# -> UTF-8 pode representar qualquer caractere universal padrão
# do Unicode, sendo também compatível com o ASCII

# Strings - ASCII

# -> print() - Imprimir um caractere a partir do código ASCII:
def exemplo1():
  for i in range(0, 255):
    print("%c" % i)
# exemplo1()
# -> No Python, aspas simples ou duplas são intercambiáveis para 
# representar strings

# Strings - Unicode

# -> print() - Imprimir um caractere a partir do código Unicode:
def exemplo2():
  print(u'\u00ae')
  print(u'\u0061')
  print(u'\u00c7')
# exemplo2()

def exemplo3():
  print(ord("a"))
  print(ord("A"))
  print(ord("á"))
# exemplo3()

def exemplo4():
  print(chr(97))
  print(chr(65))
  print(chr(225))
  # hexadecimal
  print(chr(0xe1))
# exemplo4()

# String - aspas triplas

# -> O Python também têm a opção de aspas triplas:
# # -> """texto"""
# -> Este comando pode ser chamado de bloco de string
# -> Aspas triplas são bastante úteis para textos com múltiplas linhas 

def exemplo5():
  t = [
    [' ', ' ', ' ', ' ', 'X'],
    ['O', 'O', ' ', 'X', ' '],
    [' ', 'O', 'X', 'O', ' '],
    [' ', ' ', ' ', 'O', ' '],
    [' ', 'O', 'O', ' ', ' '],
  ]

  for i in range(4):
    print(""" {} | {} | {} | {} | {} """.format(t[i][0], t[i][1], t[i][2], t[i][3], t[i][4]))
    print("""---+---+---+---+---""")
  print(""" {} | {} | {} | {} | {} """.format(t[4][0], t[4][1], t[4][2], t[4][3], t[4][4]))
# exemplo5()

# String - índices 

# -> De uma maneira geral, strings são tuplas de caracters
# -> Podemos acessar cada caractere utilizndo o índice de sua 
# posição dentro da string

def exemplo6():
  s = "spam"
  print(s[0])
  print(s[2])
  print(s[-2])
# exemplo6()

# Strings - fatiamento (slicing)

# -> Podemos também utilizar o fatiamento (slicing) nas strings
# -> O fatiamento serve para extrairmos uma seção específica da string

def exemplo7():
  s = "spam"
  print(s[1:3])
  print(s[:3])
  print(s[1:])
# exemplo7()

# Strings - Imutabilidade

# -> As strings seguem o conceito de imutabilidade (Tupla)
# -> Não é possível alterar um único caractere de uma string
# -> Para alterarmos um ou mais caracteres de uma string, 
# normalmente criamos outra variável

def exemplo8():
  s = "spam"
  s_novo = "z" + s[1:]
  print(s_novo)
# exemplo8()

# Strings - Funções 

# -> Existem muitos métodos próprios para serem utilizados com strings
# Exemplos:

# capitalize()
# count()
# find()
# lower()
# islower()
# isdigit()
# isalpha()
# isupper()
# split()
# strip()
# replace()

# -> Assim como nas listas e tuplas, podemos usar o método len() 
# para obter o tamanho da string
# -> Tamanho significa o número de caracteres




