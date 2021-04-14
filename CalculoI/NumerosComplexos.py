# Calcule zn para n = 1, . . . , 30, sendo z0 = 0, zn = z^2n−1 + w, 
# com: (a) w = −0,1 + 0,1i, (b) w = 0,8 − 0,9i. Use 5
# casas decimais.

from math import *

# número complexo ao quadrado
# num = [real, imaginaria]
def numComplexoPot(num):
  re = (num[0]**2) - (num[1] ** 2)
  im = 2*num[0]*num[1]

  return [re, im]

def z(n, ex):
  if ex == 'a':
    w = [-0.1, 0.1]
  if ex == 'b':
    w = [0.8, 0.9]
  if n == 0:
    print('0')
    return [0, 0]
  else:
    resul = z(n-1, ex)
    
    re = resul[0]
    im = resul[1]

    [re, im] = numComplexoPot([re, im])

    re = re**2 + w[0]
    im = im**2 + w[1]

    print("{0:.5f} + {1:.5f}i".format(re, im))
    
    return [re, im]

z(5, 'a')