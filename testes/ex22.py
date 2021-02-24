nome = input("Digite seu nome completo: ")

print(nome.upper())
print(nome.lower())
space = nome.count(" ")
letras = len(nome) - space
print("Seu nome tem {} letras".format(letras))
novo_nome = nome.split(" ")
print("Seu primeiro nome tem {} letras.".format(len(novo_nome[0])))
