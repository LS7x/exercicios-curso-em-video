from time import sleep

cores = {'padrao' : '\033[m',
         'roxo'   : '\033[1;35m'}

print('{}-{}'.format(cores['roxo'], cores['padrao'])*50)
print('{}Seja bem vindo ao IMC Python!'
      '\nAgora iremos verificar seu IMC e sua saude...{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['roxo'], cores['padrao'])*50)

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)
print('Aguarde, calculando...\n')
sleep(3)

if (peso >= 1000) or (altura >= 3) or (peso <= 25) or (altura <= 0.50):
    print('{}Valor invalido, tente novamente!'.format('\033[1;31m', cores['padrao']))

elif imc < 18.5:
    print('{}Seu IMC é de {:.2f} Kg/m²!'
          '\nE você esta abaixo do peso ideal!{}'.format('\033[1;36m', imc, cores['padrao']))

elif imc == 18.5 or imc < 25:
    print('{}Seu IMC é de {:.2f} Kg/m²'
          '\nE você esta entre o peso ideal!{}'.format('\033[1;34m', imc, cores['padrao']))

elif imc == 25 or imc < 30:
    print('{}Seu IMC é de {:.2f} Kg/m²'
          '\nE você esta sobrepeso!{}'.format(cores['roxo'], imc, cores['padrao']))

elif imc == 30 or imc < 40:
    print('{}Seu IMC é de {:.2f} Kg/m²'
          '\nE você esta na obesidade!{}'.format('\033[1;33m', imc, cores['padrao']))

elif imc >= 40:
    print('{}Seu IMC é de {:.2f} Kg/m²'
          '\nE você esta na obesidade mórbida!{}'.format('\033[1;31m', imc, cores['padrao']))

