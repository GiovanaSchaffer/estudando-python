vel = int(input("Qual a velocidade do carro em Km/h: "))
if vel > 80:
    print("Você foi multado!")
    multa = (vel - 80)*7
    print("Sua multa vai custar R$ {:.2f} ".format(multa))
else:
    print("Está tudo okay!")
