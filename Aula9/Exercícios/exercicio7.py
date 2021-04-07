# Exercício 7:

# Existem restrições para que uma pessoa possa doar sangue. 
# Uma delas é relativa ao peso. Mulheres tem que pesar no 
# mínimo 50kg e homens no mínimo 60kg. Faça uma função para 
# informar se uma pessoa está ou não apta a doar sangue 
# sabendo seu sexo e seu peso. 
# O programa principal deve ler as entradas, acionar a função 
# e exibir a resposta.

def verificaDoacao(sexo, peso):
  if sexo == 'F':
    return peso >= 50
  elif sexo == 'M':
    return peso >= 60
  else:
    return False

sexo = input("Digite o sexo (F/M): ")
peso = float(input("Digite o peso: "))

if verificaDoacao(sexo, peso):
  print("A pessoa está apta")
else:
  print("A pessoa não está apta")
