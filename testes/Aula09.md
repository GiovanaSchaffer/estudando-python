# Aula09

### fateamento

frase = "Giovana"

print(frase[4]) nos retorna a letra na posição 4, portanto nos retorna "a"

print(frase[0:5]) nos retorna os caracteres da posição 0 até a posição 4, ou seja, nos retorna "Giova". Também poderiamos escrever frase[:5] que já começaria na posição inicial.

print(frase[1:]) nos retorna os caracteres da posição 1 até a posição final, ou seja, "iovana"

print(frase[::2]) no retorna os caracteres do inicio ao fim, pulando de 2 em 2, isto é, [inicio,fim,passo], nos retornaria "Goaa"

### funções 

len(frase) seria o tamanho da minha string frase, que começa no 0, ou seja, tem tamanho 6.

frase.count("a") nos retornaria quantas vezes a letra "a" aparece em frase, portanto nos retorna 2.

frase.find("i") nos retornaria a posição onde aparece pela primeira vez a letra i, ou seja, nos retornaria o valor 1.

frase.replace('Giov', 'Al') Faria com que, onde eu tivesse Giov, substitua por Al, portanto frase ficaria Alana.

frase.upper() Faria com que todas as letras se tornem maiúsculas

frase.lower() faz com que todas as letras se tornem minúsculas

frase.capitalize() Joga todos os caracteres para minúsculo e só a primeira letra fica maiúscula 

frase.title() Analisa quantas palavras tem a string e faz com que a primeira letra de todas as palavras se torne maiúscula.

frase.strip() Elimina os espaços inúteis no início e no final da string

frase.rstrip() Elimina os espaços inúteis a direita

frase.lstrip() Elimina os espaços inúteis a esquerda

frase.split() Divide a sua string considerando os espaços

ex: se eu tenho frase = "Giovana é linda"

ficaria frase[0] = Giovana, frase[1] = é, frase[2] = linda

join(frase) Junta uma coisa na outra

ex: '-'join(frase) resultaria em Giovana-é-linda

 

 







