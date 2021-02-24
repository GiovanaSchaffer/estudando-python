from random import choice
alunos = ["aluno1","aluno2","aluno3","aluno4"]
alunos[0] = input("Digite o nome do primeiro aluno: ")
alunos[1] = input("Digite o nome do segundo aluno: ")
alunos[2] = input("Digite o nome do terceiro aluno: ")
alunos[3] = input("Digite o nome do quarto e último aluno: ")

print("O aluno escolhido foi {}".format(choice(alunos)))
