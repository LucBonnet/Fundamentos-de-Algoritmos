# Exercício 6

# Escreva uma função, test_primeNão que recebe um número e 
# verifica se ele é primo ou não. A função retorna True ou 
# False. Não é necessário desenvolver o programa principal.

def test_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  else:
    return True


print( test_prime(11) )
print( test_prime(8) )