from time import sleep

cores = {'padrao':'\033[m',
         'roxo':'\033[1;35m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['roxo'], cores['padrao'])*60)
print('{}Seja bem-vindo ao seletor de palindromo'.format('\033[1m').center(60))
print('Fique avontade para digitar sua frase e verificala se ela é!{}'.format(cores['roxo']))
print('{}-{}'.format(cores['roxo'], cores['padrao'])*60)

print('{}Observações desconsidere acentuação e pontuação na frase!{}'.format('\033[1m', cores['padrao']))
frase = str(input('Digite sua frase: ').lower())

fraseInvertida = frase[::-1]
stringSemEspaco = frase.replace(' ','')
stringInvertida = stringSemEspaco[::-1]

print('Aguarde, remoldando...\n')
sleep(3)

if stringInvertida == stringSemEspaco:
    print('{}Sim, a frase é um palindromo!{}'.format(cores['verde'], cores['padrao']))
    print('A palavra original é: {}'.format(frase))
    print('{}A palavra invertida ficaria: {}{}'.format('\033[1m', fraseInvertida, cores['padrao']))

else:
    print('{}Não, a frase não é um palindromo!{}'.format(cores['vermelho'], cores['padrao']))
