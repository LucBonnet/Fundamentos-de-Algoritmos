# Exercício 5:

# O jogo deve começar solicitando a palavra secreta 
# para o usuário 1 (o usuário 1 pode entrar com letras 
# maiúsculas ou minúsculas, isto não deve influenciar 
# no jogo).

# Então, o usuário 2, deve chutar as letras da palavra
# secreta e tentar acertá-la. Lembre-se de que o 
# usuário 2 não deve poder ver a palavra secreta 
# digitada pelo usuário 1.

# O usuário 2 pode errar a letra 5 vezes. No sexto 
# erro, o jogo termina. 

# O jogo deve verificar se a letra digitada pelo 
# usuário 2 já foi ou não digitada. Letras repetidas 
# não devem contar. 

# O jogo deve também mostrar a quantidade de letras 
# da palavra secreta, assim como as letras corretas 
# em suas devidas posições.
  
def main():
  secretWord = input("Digite a palavra secreta:")

  # pula 10 linhas
  for i in range(10):
    print()

  score = 6
  shots = []
  wordShots = []
  for i in range(len(secretWord)):
    wordShots.append('-')
    print('-', end="")
  print()

  while True:
    shot = input("\nDigite uma letra:")
    if shot not in shots:
      shots.append(shot)
      
      if shot in secretWord:
        index = []
        for i in range(len(secretWord)):
          if shot == secretWord[i]:
            index.append(i)
        for i in index:
          wordShots[i] = shot
        show(wordShots, score)
        if secretWord == ''.join(wordShots):
          print('Você acertou!')
          break
      else:
        print("Você errou!")
        score -= 1
        show(wordShots, score)
        if score == 0:
          break

def show(wordShots, score):
  print('X==:==')
  print('X  :  ')
  if score == 6:
    for i in range(4):
      print('X')
  elif score == 5:
    print('X  O   ')
    for i in range(3):
      print('X')
  elif score == 4:
    print('X  O   ')
    print('X  |   ')
    for i in range(2):
      print('X')
  elif score == 3:
    print('X  O   ')
    print('X \|   ')
    for i in range(2):
      print('X')
  elif score == 2:
    print('X  O   ')
    print('X \|/  ')
    for i in range(2):
      print('X')
  elif score == 1:
    print('X  O   ')
    print('X \|/  ')
    print('X /    ')
    print('X')
  elif score == 0:
    print('X  O   ')
    print('X \|/  ')
    print('X / \  ')
    print('X')
  print('===========')
  if score != 0:
    print(''.join(wordShots))
  else:
    print('Enforcado!')

main()
