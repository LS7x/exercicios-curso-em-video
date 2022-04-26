
cores = {'padrao': '\033[m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

def deco():
    print('{}-{}'.format(cores['amarelo'], cores['padrao'])*60)

deco()
print('{}Bem-vindo ao leitor de numeral!'.format('\033[1m').center(60))
print('A regra é simples, digite um número de 0 a 20!'.center(60))
deco()

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('Digite o seu numero: '))

    if 0 <= valor <= 20:
        break

    else:
        print('{}Valor invalido, tente novamente...{}\n'.format(cores['vermelho'], cores['padrao']))

print('{}O número digitado foi {}{}'.format(cores['verde'], numero[valor], cores['padrao']))
deco()
