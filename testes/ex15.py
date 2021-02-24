d = int(input("Quantos dias foi alugado? "))
km = int(input("Quantos quilometros foram rodados? "))

c = 60*d + 0.15 * km


print("O total a pagar é de R$ {:.2f}".format(c))
