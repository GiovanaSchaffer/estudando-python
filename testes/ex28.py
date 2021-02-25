from random import choice
resp = input("Pensei em um número inteiro entre 0 e 5, você consegue adivinhar qual foi? ")
lista = ["0","1","2","3","4","5"]
ncomp = choice(lista)
if resp.upper() == "SIM":
    num = int(input("Qual número você acha que eu pensei? "))
    if num == ncomp:
        print("Você acertou!! ")
    else:
        print("Não foi dessa vez :(  eu pensei em {}".format(ncomp))

else:
    print("Que pena, quem sabe na próxima :/ ")

    
