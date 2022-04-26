from time import sleep
cores = {'padrão':'\033[m'}

print('{}-{}'.format('\033[1;31m', cores['padrão'])*70)
print('{}Seja bem-vindo! Calculo de triângulos.'
      '\nNesse programa iremos revelar as possibilidades dos triângulos.'.format('\033[1m', cores['padrão']))
print('{}-{}'.format('\033[1;31m', cores['padrão'])*70)

c1 = float(input('Digite o comprimento do 1ª lado: '))
c2 = float(input('Digite o comprimento do 2ª lado: '))
c3 = float(input('Digite o comprimento do 3ª lado: '))

print('Aguarde, calculando...\n')
sleep(3)

if (c1 < c2 + c3) and (c1 < c3 + c2) and (c2 < c3 + c1):
    print('{}É possivel formar um triângulo com os valores!{}'.format('\033[1;32m', cores['padrão']))

    if c1 == c2 == c3:
        print('{}Este triângulo é um triângulo equilátero!{}'.format('\033[1;33m', cores['padrão']))

    elif (c1 == c2) or (c1 == c3) or (c2 == c3):
        print('{}Este triângulo é um triângulo isósceles!{}'.format('\033[1;35m', cores['padrão']))

    elif c1 != c2 != c3 != c1:
        print('{}Este triângulo é um triângulo escaleno!{}'.format('\033[1;36m', cores['padrão']))

else:
    print('{}Não é possivel formar um triângulo com os valores selecionados!{}'.format('\033[1;31m', cores['padrão']))
