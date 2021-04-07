# Exercício 2:

# Escreva uma função com parâmetros chamada multiplo(x, y). 
# Esta função deve receber dois números e retornar True se o 
# primeiro for múltiplo do segundo número; a função retorna 
# False caso contrário.

multiplo = lambda x, y : y % x == 0

print(multiplo(5, 11))
print(multiplo(3, 27))
print(multiplo(7, 3247))
print(multiplo(10, 110))
