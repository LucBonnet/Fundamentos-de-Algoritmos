# Exercício 9:

# Tente refazer os exercícios 1, 2 e 3 utilizando função lambda.

# 1.
maximo = lambda x, y : x if x > y else y

print(maximo(10, 5))

# 2.
multiplo = lambda x, y : y % x == 0

print(multiplo(5, 11))

# 3.
area = lambda base, altura : (base * altura) / 2

print(area(5, 2))