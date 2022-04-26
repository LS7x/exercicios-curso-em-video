from time import sleep
cores = {'padrao':'\033[m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['vermelho'], cores['padrao'])*70)
print('{}Calculo de progressão aritmética de 10 termos!{}'.format('\033[1m', cores['padrao']).center(70))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*70)

valor = int(input('Digite o valor do 1º termo: '))
razao = int(input('Digite o valor da razão: '))

termo = valor
contador = 1
quantidade = 0
mais = 10

print('Aguarde organizando...\n')
sleep(0.8)

while mais != 0:
    quantidade += mais
    while contador <= quantidade:
        contador += 1
        print('{}'.format(termo), end=' -> ')
        termo += razao
        sleep(0.4)

    print('{}PAUSA{}'.format(cores['vermelho'], cores['padrao']))
    mais = int(input('Mais quantos termos você desja ver: '))
    print()

print('{}Foram mostrado {} termos no total!{}'.format('\033[1m', quantidade, cores['padrao']))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*70)
