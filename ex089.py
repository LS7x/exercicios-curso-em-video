from time import sleep
cores = {'padrao': '\033[m', 'ciano': '\033[1;36m', 'vermelho': '\033[1;31m'}


def deco():
    print('{}-{}'.format(cores['ciano'], cores['padrao'])*60)


deco()
print('{}Calculadora de médias da Universidade'.format('\033[1m').center(60))

contadorPessoa = 1
contador = 0

lista = []

while True:
    deco()
    nome = str(input(f'Digite o nome do {contadorPessoa}ª aluno: '))
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input('Digite a 2ª nota do aluno: '))
    deco()

    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar [S/N]:').upper().strip())

        if continuar == 'SN' or continuar == 'NS':
            continuar = ' '

    if continuar == 'N':
        break

    contadorPessoa += 1
    contador += 1

deco()
print('{}A média dos alunos foram:'.format(cores['ciano']))
deco()
print(f'{"Nª":<5}{"Nome":<15}{"Média":<10}')
deco()

for quantidade in range(0, contador + 1):
    sleep(0.3)
    print(f'{quantidade:<5}{lista[quantidade][0]:<15}{lista[quantidade][3]}')
deco()

while True:

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja visualizar as notas de algum aluno? [S/N]: ').upper().strip())

        if continuar == 'SN' or continuar == 'NS':
            continuar = ' '

    if continuar == 'N':
        deco()
        break

    while True:
        usuario = int(input('Qual é o ID da pessoa que deseja visualizar?: '))

        if usuario > contador or usuario < 0:
            print('\n{}Usuario invalido, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))

        else:
            break

    sleep(0.5)
    print(f'As notas do aluno(a) {lista[usuario][0]} são {lista[usuario][1]} e {lista[usuario][2]}')
    deco()
