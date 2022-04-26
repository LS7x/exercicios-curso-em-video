from random import shuffle

print('\033[1;36m-\033[m'* 60)
print('''\033[0;37mSeja bem-vindo ao seletor de alunos!
Iremos escolher 5 alunos para realiza a apresentação, ok?''')
print('\033[1;36m-\033[m'* 60)

a1 = str(input('Digite o nome do {}1ª{} aluno(a): '.format('\033[1;32m','\033[m')))
a2 = str(input('Digite o nome do {}2ª{} aluno(a): '.format('\033[1;32m','\033[m')))
a3 = str(input('Digite o nome do {}3ª{} aluno(a): '.format('\033[1;32m','\033[m')))
a4 = str(input('Digite o nome do {}4ª{} aluno(a): '.format('\033[1;32m','\033[m')))
lista = [a1,a2, a3, a4]
shuffle(lista)

print('A lista de apresentação sera de: {}'.format(lista))
