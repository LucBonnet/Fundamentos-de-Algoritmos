# Exercício 3:

# Implemente uma função que receba um nome completo 
# e apresente apenas o último nome e o 1° nome na 
# seguinte forma:

# último, 1° nome.

def nomeCitacao(nome):
  nome = nome.split(' ')
  print(nome[len(nome)-1] + ', ' + nome[0])

nomeCitacao("Rafael Paes Oliveira")