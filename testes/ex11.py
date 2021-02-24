l = int(input("Digite a largura da parede: "))
a = int(input("Digite a altura da parede: "))
s = l*a
print("A área da parede é de {} m quadrados".format(s))
print("Sabendo que cada litro de tinta pinta uma área de 2m quadrados\nSerão necessários {} litros de tinta para pintar toda parede.".format(s//2))
