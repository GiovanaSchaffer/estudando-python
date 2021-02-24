frase = input("Digite uma frase: ")
frase1 = frase.upper()
contador = frase1.count("A")
pos = frase1.find("A")+1
print("A letra 'a' aparece {} vezes ".format(contador))
print("Esta letra aparece pela primeira vez na posição {}.".format(pos))
print("A letra 'a' aparece pela última vez na posição {}".format(frase1.rfind("A")+1))
