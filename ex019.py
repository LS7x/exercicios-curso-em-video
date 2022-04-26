from random import choice

a1 = input('Digite o nome do 1ª aluno(a): ')
a2 = input('Digite o nome do 2ª aluno(a): ')
a3 = input('Digite o nome do 3ª aluno(a): ')
a4 = input('Digite o nome do 4ª aluno(a): ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O aluno escolhido para apagar o quadro foi: {}'.format(escolhido))
