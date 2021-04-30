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
      print("Valor invalido!\nTente novamente\n")
      continue

# Criar um novo usuário com pontuação, vitórias e derrotas igual a zero
def criaJogador(nome=""):
  if nome == "":
    nome = input("Digite o nome do novo jogador: ")
  
  # Verifica se um arquivo para esse jogador já existe
  if os.path.isfile("{0}.txt".format(nome)):
    print("Jogador ja registrado\n")
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
    print("Pontuacao de {}: ".format(nome))
    # Pegar as linhas do arquivo para leitura
    historico = file.readlines()
    vitorias = historico[0].strip()
    derrotas = historico[1].strip()
    print("Vitorias: {0}".format(vitorias))
    print("Derrotas: {0}\n".format(derrotas))
  else:
    print("Jogador {} nao existe".format(nome))

def start():
  jogador1 = input("Digite o nome do primeiro jogador (X): ")
  
  # Verifica se o jogador digitado existe
  if not os.path.isfile("{0}.txt".format(jogador1)):
    print("Esse jogador nao existe!")
    criaJogador(jogador1)

  jogador2 = input("Digite o nome do segundo jogador (O): ")

  # Verifica se o jogador digitado existe
  if not os.path.isfile("{0}.txt".format(jogador2)):
    print("Esse jogador nao existe!")
    criaJogador(jogador2)

  # Armazena o jogador que irá jogar no momento (0 = jogador1 e 1 = jogador2)
  jogador = 0

  tabuleiro = []
  # Preenche todo o tabuleiro com vazio (" ")
  for i in range(5):
    linha = []
    for j in range(5):
      linha.append(" ")
    tabuleiro.append(linha)
  
  while True:
    if jogador == 0: 
      print("Vez de {} (X):".format(jogador1))
    else:
      print("Vez de {} (O):".format(jogador2))
    
    print()

    while True:
      # Recebe a linha da jogada
      linha = input("Digite a linha desejada (0 a 4): ")
      # verica se o valor digitado está entre 1 e 5
      while linha not in ["0", "1", "2", "3", "4"]:
        linha = input("Valor invalido!\nDigite a linha desejada (0 a 4): ")
      
      # Recebe a coluna da jogada
      coluna = input("Digite a coluna desejada (0 a 4): ")
      # verica se o valor digitado está entre 1 e 5
      while coluna not in ["0", "1", "2", "3", "4"]:
        coluna = input("Valor invalido!\nDigite a coluna desejada (0 a 4): ")
      
      linha = int(linha)
      coluna = int(coluna)

      if not tabuleiro[linha][coluna] == " ":
        print("Esta posição já está preenchida\n")
      else: 
        break

    if jogador == 0:
      tabuleiro[linha][coluna] = "X"
    else:
      tabuleiro[linha][coluna] = "O"

    # mostra o tabuleiro 
    mostraTabuleiro(tabuleiro)

    # Verifica se alguem ganhou ou se o jogo empatou
    # -1: Nada aconteceu
    #  0: Alguém ganhou
    #  1: Empate
    if verificaTabuleiro(tabuleiro) == 0:
      perdedor = ""
      vencedor = ""
      if jogador == 0: 
        vencedor = jogador1
        perdedor = jogador2
        print(jogador1 + " (X) ganhou!")
      else:
        vencedor = jogador2
        perdedor = jogador1
        print(jogador2 + " (O) ganhou!\n")

      # pega os valores atuais de vitorias e derrotas do jogador vencedor
      file = open("{}.txt".format(vencedor), "r")
      historico = file.readlines()
      file.close()
      vitorias = int(historico[0].strip())
      derrotas = int(historico[1].strip())
      # adiciona uma vitória
      vitorias += 1

      # Atualiza o arquivo do jogador vencedor
      file = open("{}.txt".format(vencedor), "w")
      file.write("{}\n".format(vitorias))
      file.write("{}\n".format(derrotas))
      file.close()

      # pega os valores atuais de vitorias e derrotas do jogador perdedor
      file = open("{}.txt".format(perdedor), "r")
      historico = file.readlines()
      file.close()
      vitorias = int(historico[0].strip())
      derrotas = int(historico[1].strip())
      # adiciona uma derrota
      derrotas += 1

      # Atualiza o arquivo do jogador perdedor
      file = open("{}.txt".format(perdedor), "w")
      file.write("{}\n".format(vitorias))
      file.write("{}\n".format(derrotas))
      file.close()
      break
    elif verificaTabuleiro(tabuleiro) == 1:
      print("O jogo empatou!")
      break

    # muda o jogador atual
    if jogador == 0:
      jogador = 1
    else:
      jogador = 0

# mostra o tabuleiro na tela
def mostraTabuleiro(tabuleiro):
  print()

  # Percorre todas a linhas e colunas do tabuleiro para mostra-lo 
  for i in range(4):
    print(""" {} | {} | {} | {} | {} """.format(tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2], tabuleiro[i][3], tabuleiro[i][4]))
    print("""---+---+---+---+---""")
  print(""" {} | {} | {} | {} | {} """.format(tabuleiro[i+1][0], tabuleiro[i+1][1], tabuleiro[i+1][2], tabuleiro[i+1][3], tabuleiro[i+1][4]))

  print()

# função para verificar se alguem ganhou ou se o jogo empatou
# -1: Nada aconteceu
#  0: Alguém ganhou
#  1: Empate
def verificaTabuleiro(tabuleiro):
  # Verifica todas as linhas para verficar se existem 4 simbolos iguais em sequencia  
  cont = 0
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[0])-1):
      if tabuleiro[i][j] == tabuleiro[i][j+1] and not tabuleiro[i][j] == ' ':
        cont += 1
        if cont == 3:
          return 0
      else:
        cont = 0
    cont = 0
  
  # Verifica todas as colunas para verficar se existem 4 simbolos iguais em sequencia  
  cont = 0
  for i in range(len(tabuleiro[0])):
    for j in range(len(tabuleiro)-1):
      if tabuleiro[j][i] == tabuleiro[j+1][i] and not tabuleiro[j][i] == ' ':
        cont += 1
        if cont == 3:
          return 0
      else:
        cont = 0
    cont = 0

  # vitórias possíveis nas diagonais:
  d = [
    [[0,0], [1,1], [2,2], [3,3]],
    [[1,1], [2,2], [3,3], [4,4]],
    [[0,4], [1,3], [2,2], [3,1]],
    [[1,3], [2,2], [3,1], [4,0]],
    [[1,0], [2,1], [3,2], [4,3]],
    [[0,1], [1,2], [2,3], [3,4]],
    [[0,3], [1,2], [2,1], [3,0]],
    [[1,4], [2,3], [3,2], [4,1]],
  ]

  # percorre as posições do tabuleiro necessarias e verifica se os itens são iguais
  cont = 0
  for i in range(len(d)):
    diagonal = []
    for j in range(len(d[0])):
      diagonal.append(tabuleiro[d[i][j][0]][d[i][j][1]])
    for v in range(len(diagonal)-1):
      if diagonal[v] == diagonal[v+1] and not diagonal[v] == " ":
        cont += 1
        if cont == 3:
          return 0
      else:
        cont = 0
    cont = 0  

  # Verifica se o jogo empatou
  cont = 0
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[0])):
      if not tabuleiro[i][j] == " ":
        cont += 1
      else:
        cont = 0
  if cont == 25:
    return 1
        
        
  return -1

main()

