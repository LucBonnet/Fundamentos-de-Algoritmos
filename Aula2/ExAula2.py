# Ex 1
def ex1():
  tf = float(input("Digite a temperatura em graus Fahrenheit: "))

  tc = (5 * (tf-32) / 9)

  print("Temperatura em graus Celsius =", round(tc, 1))

# Ex 2
def ex2():
  n_lab = float(input("Digite a nota de LAB: "))
  n_p1 = float(input("Digite a nota de P1: "))
  n_p2 = float(input("Digite a nota de P2: "))

  m = (n_lab + 2 * n_p1 + 3 * n_p2) / 6

  print("M =", round(m, 2))

# Ex 3
def ex3():
  n_dec = int(input("Digite um valor da base decimal: "))

  n_bin = ""
  n = n_dec
  while (n >= 2):
    n_bin += str(n % 2)
    n //= 2

  n_bin += str(n) + "b0"

  # abcdefghijklmn"[2:10:2] -> cegi
  # abcdefghijklmn"[0:14:3] -> adgjm
  print("Binário=", n_bin[::-1])
  #ou 
  print("Binário=", bin(n_dec))

# Ex 4
def ex4():
  c = float(input("Entre o comprimento da sala em metros: "))
  l = float(input("Entre a largura da sala em metros: "))

  print("A área da sala é {} metros quadrados".format(c*l))

# Ex 5
def ex5():
  b = float(input("Digite o valor da Base: "))
  h = float(input("Digite o valor da altura: "))
  a = (b * h) / 2

  print("Área do triângulo = ", a)

# Ex 6
def ex6():
  s = float(input("Digite o salário do funcionário: "))
  aumen = s + s * (25/100)

  print("Salário com aumento =", aumen)

# Ex 7
def ex7():
  t = int(input("Digite o tempo em horas: "))
  d = float(input("Digite a distância percorrida: "))

  v = d/t

  print("Velocidade média = {} Km/h".format(v))

# Ex 8
def ex8():
  qtd_ovos = int(input("Digite a quantidade de ovos: "))

  print("Você pode fazer {} bolos".format(qtd_ovos//5))

# Ex 9
def ex9():
  n = int(input("Digite um número positivo: "))
  s = (n * (n + 1)) / 2
    
  print("A soma dos primeiros {} números positivos é {}".format(n, s))

#Ex 10
def ex10():
  t_imposto = 18/100
  t_gorjeta = 10/100

  v_refeicao = float(input("Digite o custo da refeição: "))
  v_total = v_refeicao + v_refeicao * t_imposto + v_refeicao * t_gorjeta

  print("O valor total da refeição é: {:.2f}".format(v_total))
  print("O valor do imposto é: {:.2f}".format(v_refeicao * t_imposto))
  print("O valor da gorjeta é: {:.2f}".format(v_refeicao * t_gorjeta))


ex10()