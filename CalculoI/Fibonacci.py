# n: Número de termos desejados
def fibonacci(n):
  a = 1
  b = 1
  k = 1
  while k <= n:
    print(a, end=' ')
    # a, b = b, a+b
    temp = a
    a = b
    b = b + temp
    
    k += 1

fibonacci(20)