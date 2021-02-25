dist = float(input("Qual será a distância da sua viagem em quilômetros? "))
if dist <= 200:
    preco = dist*(0.5)
else:
    preco = dist*(0.45)
print("O preço da sua passagem é de R${:.2f}".format(preco))
