salario = float(input("Qual o valor de seu salário? "))
if salario>1250:
    aumento = (salario*10)/100
    salario = salario + aumento
else:
    aumento = (salario*15)/100
    salario = salario + aumento
print("Seu novo salário é de R${:.2f}".format(salario))
