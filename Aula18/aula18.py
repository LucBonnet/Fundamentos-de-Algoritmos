# Módulos

# -> Para o Python, Módulos são arquivos fonte 
# que podem ser importados para um programa
# -> Podem conter qualquer estrutura do Python
# e são executador quando importados
# -> Um módulo é um arquivo .py que pode conter:
  # -> Funções
  # -> Variáveis e Constantes
# -> Os módulos são carregados através da 
# instrução import
# -> Desta forma, ao usar alguma estrutura do
# módulo, é necessário identificá-lo
  # -> Isto é chamado de importação absoluta

# Exemplos:
# import os
# os.remove('arquivo.txt')

# -> Também é possível importar de forma relativa
# utilizando as palavras-caves from import

# Exemplo:
# from os import remove
# remove('arquivo.txt')

# -> Ainda usanso a importação relativa, podemos 
# usar o * para importar tudo o que está no módulo

# Exemplo:
# from os import *
# remove('arquivo.txt')

# -> A importação relativa com o * não é 
# recomendada, pois pode gerar problemas, como 
# ofuscação de variáveis

# Vantagens dos Módulos

# -> Deixa o programa mais organizado
# -> Permite a reusabilidade
# -> A criação de módulos com funções também evita
# a criação de variáveis globais
  # -> A criação de variáveis globais é, muitas 
  # vezes, vista como uma má prática de programação

# Criando seus próprios módulos

# Módulo: arquivo "calculo.py"

# # função média recebe lista como parametro
# def media(lista):
#   return float(sum(lista) / len(lista))

# Importação absoluta:

# import calculo
# l = [10, 15, 87, 14, 98, 41, 30, 36]
# print(calculo.media(l))

# Importação relativa:

# from calculo import media
# l = [10, 15, 87, 14, 98, 41, 30, 36]
# print(media(l))

# -> Módulos são arquivos .py
# -> Como garantimos que um programa principal 
# não será importado em outro arquivo .py?
# -> Utilizamos a variável especial __name__
# -> __name__ indica o nome do contexto em que 
# o módulo está sendo executado
# -> Quando um módulo é diretamente executado, 
# __name__ é definido como "__main__"
# -> Quando o módulo é importado, __name__ fica 
# igual ao nome do módulo, ou seja, do arquivo
# -> Logo, podemos incluir uma condição para 
# rodar nosso main:

# from calculo import media
#
# def main():
#   l = [10, 15, 87, 14, 98, 41, 30, 36]
#   print(media(l))
#
# if __name__ == "__main__":
#   main()

# Biblioteca padrão

# -> O Python vem com vários módulos distribuídos 
# por padrão com o interpretador
# -> Alguns módulos importantes da biblioteca 
# padrão são:
  # -> Matemática: math, random
  # -> Sistema: os, sys, zipfile
  # -> Tempo: time, datetime

# Pacotes (Packages)

# -> De uma forma simples, um pacote é uma 
# coleção de módulos
# -> Quando os módulos aumentam de tamanho, 
# podemos dividí-los em pacotes
# -> Módulos são estruturados em arquivos, 
# enquanto que, pacotes são estruturados em 
# pastas
# -> Todos os pacotes devem conter um arquivo 
# __init__.py
# -> Os arquivos __init__.py servem para que o 
# interpretador possa identificar quais 
# diretórios são pacotes e quais não são


