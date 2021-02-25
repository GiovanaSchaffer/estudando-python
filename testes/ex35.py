l1 = int(input("Qual será o comprimento da primeira reta? "))
l2 = int(input("Qual será o comprimento da segunda reta? "))
l3 = int(input("Qual o comprimento da terceira reta? "))
if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    if l1-l2<l3 and l2-l3<l1 and l1-l3<l2:
        print("Formam um triângulo!")
else:
    print("Não formam triângulo.")
