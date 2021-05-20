# Exercício 3:

# Embora a popularidade dos cheques como método de pagamento 
# tenha diminuído nos últimos anos, algumas empresas ainda os 
# emitem para pagar funcionários ou fornecedores. A quantia que 
# está sendo paga normalmente aparece duas vezes em um cheque, 
# com uma ocorrência escrita com números e outra ocorrendo com 
# palavras. Repetir o valor em dois formulários diferentes torna 
# muito mais difícil para um funcionário ou fornecedor 
# inescrupuloso modificar o valor do cheque antes de depositá-lo. 
# Neste exercício, sua tarefa é criar uma função (chamada 
# numero_texto) que receba um número inteiro entre 0 e 999 como seu 
# único parâmetro e retorne uma string contendo as palavras em 
# português para esse número. Por exemplo, se o parâmetro para 
# a função for 142, sua função deve retornar “cento e quarenta e 
# dois”. Use um ou mais dicionários para implementar sua solução, 
# em vez de grandes construções if / elif / else. 

def numero_texto(num):
  centenas_dic = {
    100: 'cento',
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seiscentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos',
  }

  dezenas_dic = {
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
  }

  unidades_dic = {
    1: 'um',
    2: 'dois',
    3: 'tres',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
  }

  centena = (num // 100) * 100
  num = num - centena
  dezena = (num // 10) * 10
  num = num - dezena
  unidade = num

  text = []

  if centena in centenas_dic:
    text.append(centenas_dic[centena])
  
  if dezena + unidade in dezenas_dic:
    text.append(dezenas_dic[dezena + unidade])
  else:
    if dezena in dezenas_dic:
      text.append(dezenas_dic[dezena])
    if unidade in unidades_dic:
      text.append(unidades_dic[unidade])
  

  print(' e '.join(text))

n = int(input("Digite um número entre 0 e 999: "))
numero_texto(n)