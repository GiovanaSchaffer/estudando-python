import random
alunos = ["aluno1","aluno2","aluno3","aluno4"]
alunos[0] = input("Qual o nome do primeiro aluno? ")
alunos[1] = input("Qual o nome do segundo aluno? ")
alunos[2] = input("Qual o nome do terceiro aluno? ")
alunos[3] = input("Qual o nome do quarto aluno? ")
random.shuffle(alunos)
print("A ordem de apresentação será: {}".format(alunos))
