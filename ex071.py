from time import sleep
cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m'}

def linha_deco():
    print('{}-{}'.format(cores['amarelo'], cores['padrao'])*65)

linha_deco()
print('{}Bem-vindo ao Python Bank'.format('\033[1m').center(65))
print('Este caixa esta funcionando somente para saque!{}'.format(cores['padrao']).center(65))
linha_deco()

print('{}Este caixa possue somente notas nos valores asseguir:'.format(cores['amarelo']).center(70))
print('R$ 50, R$20, RS10 e R$1{}'.format(cores['padrao']).center(65))
linha_deco()

valor = int(input('Digite o valor do saque: R$'))
print('Aguarde, calculando...')
sleep(2)
linha_deco()

total = valor
contador = 0
nota = 50

while True:

    if total >= nota:
        total -= nota
        contador += 1

    else:
        if contador > 0:
            sleep(0.5)
            print('{}A quantidade de celulas nos valores de R${} são: {}'
                  .format(cores['amarelo'], nota, contador))

        if nota == 50:
            nota = 20

        elif nota == 20:
            nota = 10

        elif nota == 10:
            nota = 1

        contador = 0
        if total == 0:
            break

linha_deco()
print('{}Volte sempre!{}'.format(cores['amarelo'], cores['padrao']))
