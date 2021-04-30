palavra = input("Digite uma palavra: ")
palavra = palavra.replace(' ', '')
if palavra == palavra[::-1]:
  print("Essa Palavra é um palindromo")
else:
  print("Essa palavra não é um palindromo")