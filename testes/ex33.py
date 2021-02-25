ano = int(input("Digite um ano: "))
if ano%4 == 0:
    if ano%100==0:
        if ano%400==0:
            print("É Bissexto!")
        else:
            print("Não é Bissexto")
    print("É Bissexto!")
else:
    print("Não é Bissexto")
