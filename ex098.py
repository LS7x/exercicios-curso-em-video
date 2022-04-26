from time import sleep

cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'vermelho': '\033[1;31m'}


def deco():
    print(f'{cores["vermelho"]}-{cores["padrao"]}' * 70)


deco()
print(f'{cores["negrito"]}Efetuando contagem de números utilizando funções!'.center(70))
deco()


def contador(inicio, fim, passo):

    if passo < 0:
        passo = (-passo)

    if passo == 0:
        passo += 1

    print(f'Efetuando contagem de {inicio} até {fim} de {passo} em {passo}:')

    if inicio > fim:
        if passo > 0:
            passo = (-passo)

        for numero in range(inicio, fim - 1, passo):
            print(numero, end=' ')
            sleep(0.5)
        print('FIM!')
        deco()

    else:
        for numero in range(inicio, fim + 1, passo):
            print(numero, end=' ')
            sleep(0.5)
        print('FIM!')
        deco()


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicioPlayer = int(input('Digite o valor de ínicio: '))
fimPlayer = int(input('Digite o valor do final: '))
passoPlayer = int(input('Digite o valor do passo: '))
deco()

contador(inicioPlayer, fimPlayer, passoPlayer)
