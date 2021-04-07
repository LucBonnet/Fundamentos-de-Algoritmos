# Exercício 4

# Em uma determinada jurisdição, as tarifas de táxi consistem 
# em uma tarifa básica de R$ 10.00, mais R$ 0.50 para cada 125 
# metros percorridos. Escreva uma função que considere a
# distância percorrida (em quilômetros inteiros) como seu único 
# parâmetro e retorne a tarifa total como seu único resultado. 
# Escreva um programa principal em que a quantidade de km será 
# digitada e onde a função será chamada.

# Calcula a tarifa
def tarifa(d):
  dkm = d * 1000
  tarifa = 10 + ((dkm/125) * 0.5)
  return tarifa

def main():
  d = int(input("Digite a quantidade de quilômetros: "))
  print('Tarifa %.2f' % tarifa(d))

main()
