# Arquivos

# -> Utilizar arquivos é uma forma de garantir o 
# armazenamento permanente dos dados que são importantes 
# no seu programa, pois nenhuma variável, nem mesmo a 
# lista , continua existindo depois que o programa 
# termina
# -> Então, utilizar um arquivo é uma maneira excelente 
# de trabalhar com a entrada e a saída de dados para os 
# programas
# -> Arquivos são linhas de texto, normalmente salvos com a
# extensão .txt ou .dat
# -> Na programação, assim como na nossa interação com o 
# computador, o primeiro passo para acessar um arquivo é 
# abri-lo
# -> Para abrir o arquivo, utilizamos a função open
# Ex: arquivo = open("teste.dat", "w")

# # -> A variável arquivo salva o arquivo em si. é por meio 
# desta variável que executamos as funções de escrita e leitura
# # -> open() tem dois parâmetros: nome do arquivo e modo de acesso

# Modos de Acesso:

# Modo | Operação
# r    | leitura(read)
# w    | escrita(write)
# a    | escrita, preservando o conteúdo existente (append)
# +    | atualização (combinando com r ou w)

# Arquivos - Escrita:

# -> Para escrever no arquivo, utilizamos o método write, 
# que vai ser chamado pela variável arquivo :
# # Ex: arquivo.write("texto a ser escrito no arquivo")
# -> O método write funciona de maneira similar que o 
# print com marcadores (%d, %f, %s), porém precisamos 
# sempre incluir o "\n" quando queremos ir para a 
# próxima linha
# -> Depois que escrevemos no arquivo, precisamos fechá-lo,
# utilizando o método close
# -> É sempre importante fechar o arquivo para informar ao 
# Sistema Operacional que não vamos mais utilizá-lo
# Muias vezes, o Sistema Operacional salva as informações que
# queremos escrever em uma memória auxiliar e deixa a operação
# de escrever realmente no arquivo só quando informamos que 
# que vamos fechá-lo
# -> Então, se não fechamos, corremos o risco de perder o que 
# gostaríamos de escrever

# Arquivos - Leitura

# -> Para ler do arquivo, precisamos seguir o mesmo 
# procedimento:
# # -> Abrir o arquivo em modo leitura "r"
# # -> Utilizar um método para ler o arquivo
# # -> Fechar o arquivo com o método close

# -> Para ler do arquivo, podemos utilizar o método 
# readlines()

