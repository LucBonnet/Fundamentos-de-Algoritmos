# Exercício 4:

# Faça um programa para criar uma lista de 10 elementos inteiros e 
# apresentar todos os conteúdos que forem maiores que a soma de dois 
# de seus antecessores

def main():
  l = []
  for i in range(10):
    l.append(int(input('Digite um numero inteiro: ')))
  
  n = []
  for i in range(len(l)):
    if i >= 2:
      if l[i] > l[i-1] + l[i-2]:
        n.append(l[i])

  print(n)
  
main()