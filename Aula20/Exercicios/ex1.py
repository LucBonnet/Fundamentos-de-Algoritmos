# Exercício 1:

# Escreva uma função chamada procuraReversa que 
# encontre todas aschaves, em um dicionário, que 
# estão associadas a um valor específico. A função 
# receberá o dicionário e o valor a procurar como 
# seus únicos parâmetros. A função retornará uma 
# lista (possivelmente vazia) de chaves associadas 
# ao valor fornecido. Faça um programa principal 
# que mostra a o funcionamento da função. Seu 
# programa principal deve criar um dicionário e
# mostrar que a função procuraReversa funciona 
# corretamente quando retorna várias chaves, uma 
# única chave ou nenhuma chave

def procuraReversa(dic, valor):
  lista = []
  for chave in dic:
    if dic[chave] == valor:
      lista.append(chave)
  
  return lista


def main():
  dicionario = {
    1: 'um',
    2: 'dois',
    3: 'tres',
    4: 'quatro',
    5: 'um',
    6: 'um'
  }

  lista = procuraReversa(dicionario, 'seis')
  print(lista)

  lista = procuraReversa(dicionario, 'dois')
  print(lista)

  lista = procuraReversa(dicionario, 'um')
  print(lista)

main()