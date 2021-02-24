catop = int(input("Digite o valor do cateto oposto: "))
catad = int(input("Digite o valor do cateto adjacente: "))
hip = catop**2 + catad**2
hip = hip**(1/2)
print("O valor da hipotenusa é de {:.2f}".format(hip))
