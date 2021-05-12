# Exercício 3:

# Exercício de Data Science – Um dos 
# processos de Data Science é a 
# preparação de dados, nesse processo 
# deve-se coletar, limpar, combinar, 
# normalizar os dados, para que possam 
# ser utilizados nos processo de 
# análise, treinamentos, etc.

# Escreva um módulo em Python com uma 
# função que lê o arquivo 
# annotations.csv que possui informações 
# de um DataSet de imagens que serão 
# utilizados para treinamento de um 
# algoritmo de Detecção de Objetos. 
# Crie uma função que deverá remover 
# todos as classes (class), deixando 
# somente a classe ball e deve também 
# remover as colunas referentes ao 
# tamanho da imagem (width, height). 
# Crie um programa principal (função 
# main) que use as duas funções para 
# escrever um novo arquivo.

from arquivo import ler, retiraClasseTamanho

def main():
  nome = input("Digite o nome do arquivo com o extensão: ")

  linhas = retiraClasseTamanho(ler(nome))

  for linha in linhas:
    print(linha[0].strip())
    print()

if __name__ == "__main__":
  main()