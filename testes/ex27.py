nome = input("Digite seu nome completo: ")
nome1 = nome.split()
tamanho = len(nome1)
print("Primeiro = {}\nÚltimo = {}".format(nome1[0],nome1[tamanho-1]))
