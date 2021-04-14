# Exercício 7

# Neste exercício, você criará um programa que lê palavras do usuário 
# até que o usuário entre com uma linha em branco. Após o usuário 
# digitar uma linha em branco, seu programa deve exibir cada palavra 
# digitada pelo usuário exatamente uma vez. As palavras devem ser 
# exibidas na mesma ordem em que foram inseridas. Por exemplo, se o 
# usuário inserir:

# first, second, first, third, second
# Saída:
# first, second, third

def main():
  l = []
  while True:
    p = input("Digita uma palavra: ")
    if p == '':
      break
    else:
      l.append(p)
  
  n = []
  for item in l:
    if not item in n:
      n.append(item)
      print(item)

main()