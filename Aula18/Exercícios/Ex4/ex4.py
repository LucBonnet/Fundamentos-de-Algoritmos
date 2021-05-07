# Exercício 4:

# Neste exercício, você deve programar um módulo 
# composto por 4 funções que, juntas, servirão 
# para determinar se uma senha é boa ou não. Uma 
# boa senha deve ter:
#   a. Pelo menos 8 caracteres (1ª função)
#   b. Pelo menos uma letra maiúscula (2ª função)
#   c. Pelo menos uma letra minúscula (3ª função)
#   d. Pelo menos um número (4ª função)

# Cada função deve retornar true ou false para a 
# senha recebida.Faça também um programa principal 
# que leia uma senha do usuário, chame cada 
# função de verificação e relate se a senha 
# é boa ou não. 

from verificaSenha import letraMaiuscula, letraMinuscula, minCaracteres, temNumero

def main():
  senha = input("Digite sua senha: ")

  cont = 0
  if letraMaiuscula(senha):
    cont += 1
  if letraMinuscula(senha):
    cont += 1
  if minCaracteres(senha):
    cont += 1
  if temNumero(senha):
    cont += 1
  
  if cont == 4:
    print("A senha é boa")
  else:
    print("A senha não é boa")

if __name__ == "__main__":
  main()