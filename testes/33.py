n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
lista = [n1,n2,n3]
if n1>n2 and n1> n3:
    print(n1,"É o maior número")
if n2>n1 and n2>n3:
    print(n2,"É o maior número")
if n3>n1 and n3>n2:
    print(n3,"É o maior número")

if n1<n2 and n1<n3:
    print(n1,"É o menor número")
if n2<n1 and n2<n3:
    print(n2,"É o menor número")
if n3<n1 and n3<n2:
    print(n3,"É o menor número")
