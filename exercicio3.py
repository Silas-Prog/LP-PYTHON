#concatenar e strings dinamicas:
nome=str(input("Informe o seu nome: "))
print("Nome informado: %s" % nome)

sobrenome=str(input("Informe o seu sobrenome: "))
print("Sobrenome informado: %s" % sobrenome)

espaco = " "

print("Seu nome é:" % nome + espaco + sobrenome)
print("Aguarde estamos procurando seu cadastro.")

idade=int(input("Informe a sua idade: "))
print("Idade informada: %i" % idade)
print("")
genero=str(input("Agora você irá informar o seu genero. 0 para feminino e 1 para masculino."))
print("Genero informado:", genero)
print("Processo de identificação concluido.")


print("Bem vindo, Sr. %s" % nome + espaco + sobrenome)
