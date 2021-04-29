import os.path

# Função principal que irá mostrar o menu para definir a opção desejada
def main(): 
  while True:
    print("- Menu ------------------ Jogo da Velha -")
    print("|                                       |")
    print("| O que você deseja fazer?              |")
    print("| 1 - Criar novo jogador                |")
    print("| 2 - Exibir pontuação                  |")
    print("| 3 - Excluir jogador                   |") 
    print("| 4 - Iniciar um partida                |")
    print("| 5 - Sair                              |")
    print("-----------------------------------------")

    # Recebe a opção desejada
    op = input("Digite o número da opção desejada: ")
    print()

    # Verifica o valor inserido para chamar uma função específica
    if op == "1":
      criaJogador()
    elif op == "2":
      mostraPontuacao()
    elif op == "3":
      deletaJogador()
    elif op == "4":
      start()
    elif op == "5":
      break
    else:
      # Caso a opção digitada não exista, o loop rodara novamente para pedir ums opção válida
      print("Valor inválido!\nTente novamente\n")
      continue

# Criar um novo usuário com pontuação, vitórias e derrotas igual a zero
def criaJogador(nome=""):
  if nome == "":
    nome = input("Digite o nome do novo jogador: ")
  
  # Verifica se um arquivo para esse jogador já existe
  if os.path.isfile("{0}.txt".format(nome)):
    print("Jogador já registrado\n")
  else:
    print("Registrando o jogador {0}\n".format(nome))
    file = open("{0}.txt".format(nome), "w")
    file.write("0\n") # pontuação\vitórias
    file.write("0\n") # derrotas
    file.close()
    print("Jogador {0} criado com sucesso!\n".format(nome))

# Deletar usuário
def deletaJogador():
  nome = input("Digite o nome do jogador a ser excluido: ")
  
  # Verifica se um arquivo para esse jogador existe
  if os.path.isfile("{0}.txt".format(nome)):
    print("Excluindo o jogador {0}\n".format(nome))
    os.remove("{0}.txt".format(nome))
  else:
    print("Jogador {0} não existe\n".format(nome))

# Ler a pontuação de um jogador
def mostraPontuacao():
  nome = input("Digite o nome do jogador: ")

  # Verifica se o jogador existe
  if os.path.isfile("{0}.txt".format(nome)):
    file = open("{0}.txt".format(nome), "r")
    print("Pontuação de {}: ".format(nome))
    # Pegar as linhas do arquivo para leitura
    historico = file.readlines()
    vitorias = historico[0].strip()
    derrotas = historico[1].strip()
    print("Vitórias: {0}".format(vitorias))
    print("Derrotas: {0}\n".format(derrotas))
  else:
    print("Jogador {} não existe".format(nome))

def start():
  jogador1 = input("Digite o nome do primeiro jogador: ")
  
  # Verifica se o jogador existe
  if not os.path.isfile("{0}.txt".format(jogador1)):
    print("Esse jogador não existe!")
    criaJogador(jogador1)

  jogador2 = input("Digite o nome do segundo jogador: ")

  # Verifica se o jogador existe
  if not os.path.isfile("{0}.txt".format(jogador2)):
    print("Esse jogador não existe!")
    criaJogador(jogador2)

  # Armazena o jogador que irá jogar (0 = jogador1 e 1 = jogador2)
  turno = 0

  tabuleiro = []

  for i in range(5):
    linha = []
    for j in range(5):
      linha.append(" ")
    tabuleiro.append(linha)
  
  while True:
    mostraTabuleiro(tabuleiro)

    if turno == 0: 
      print("Vez do Jogador 1 (X):")
    else:
      print("Vez do jogador 2 (O):")
    
    print()

    while True:
      # Recebe a linha da jogada
      linha = int(input("Digite a linha desejada (1 a 5): "))
      # verica se o valor digitado está entre 1 e 5
      while linha not in [1, 2, 3, 4, 5]:
        linha = int(input("Valor inválido!\nDigite a linha desejada (1 a 5): "))
      
      # Recebe a coluna da jogada
      coluna = int(input("Digite a coluna desejada (1 a 5): "))
      # verica se o valor digitado está entre 1 e 5
      while coluna not in [1, 2, 3, 4, 5]:
        coluna = int(input("Valor inválido!\nDigite a coluna desejada (1 a 5): "))
      
      if not tabuleiro[linha][coluna] == " ":
        print("Esta posicao ja esta preenchida")
      else: 
        break

    


    

# mostra o tabuleiro na tela
def mostraTabuleiro(tabuleiro):
  # Percorre todas a linhas e colunas do tabuleiro para mostra-lo 
  for i in range(len(tabuleiro)-1):
    for j in range(len(tabuleiro[0])-1):
      print(" {} |".format(tabuleiro[i][j]), end="")
    print(" {}".format(tabuleiro[i][j+1]))
    print("---+---+---+---+---")
  for i in range(len(tabuleiro)-1):
    print(" {} |".format(tabuleiro[i][j+1]), end="")
  print(" {}".format(tabuleiro[i+1][j+1]))

  print()

main()

