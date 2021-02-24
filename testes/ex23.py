num = int(input("Digite um número entre 0 e 9999: "))

if (0<=num<=9999):
    milhar = num//1000
    centena = (num - milhar*1000)//100
    dezena = (num-milhar*1000-centena*100)//10
    unidade = num-milhar*1000-centena*100-dezena*10
    print("Unidade = {}\nDezena = {}\nCentena = {}\nMilhar = {}".format(unidade,dezena,centena,milhar))
else:
    print("Seu número foi inválido.")

