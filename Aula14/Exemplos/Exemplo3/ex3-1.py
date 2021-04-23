# Criar um arquivo com o nome e o telefone de pessoas, conforme 
# são digitados pelo usuário. O programa deve funcionar em loop até 
# que o nome digitado seja vazio.

contatos = open("contatos.dat", "a")

nome = input("Nome: ")
telefone = input("Telefone: ")

while nome != "":
  contatos = open("contatos.dat", "a")
  contatos.write("%s %s\n" % (nome, telefone))
  contatos.close()
  nome = input("Nome: ")
  if nome != "":
    telefone = input("Telefone: ")