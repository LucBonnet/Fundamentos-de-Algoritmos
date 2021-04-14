# Exercício 8:

# Faça um programa que preencha uma lista com dez números inteiros 
# aleatórios (de 0 a 100). Calcule e mostre os números superiores a 
# 50 e suas respectivas posições. O programa deverá mostrar uma 
# mensagem caso não exista nenhum número nessa condição

def main():
  l = []
  for i in range(10):
    l.append(int(input("Digite um número inteiro de 0 a 100: ")))
  
  hasNumber = False
  for i in range(len(l)):
    if l[i] > 50:
      hasNumber = True
      print(l[i], 'é maior que 50 e está na posição', i)
  
  if not hasNumber:
    print('Não existe nenhum número nesta condição')

main()