from time import sleep
cores = {'padrao':'\033[m'}

print('{}-{}'.format('\033[36m', cores['padrao'])*60)
print('{}Bem vindo a calculadora python!'
      '\nNesse quesito iremos calcular a sua media de notas!{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format('\033[36m', cores['padrao'])*60)

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2º nota: '))

print('Aguarde calculando...\n')
sleep(3)
media = (n1 + n2) / 2

if (n1 > 10 or n2 > 10) or (n1 < 0 or n2 < 0):
    print('{}Valor de nota invalido, tente novamente!{}'.format('\033[1;31m', cores['padrao']))

elif media < 5.00:
    print('{}Você obteve media de {:.1f} e infelizmente foi REPROVADO!{}'.format('\033[1;31m', media, cores['padrao']))

elif media > 7.00:
    print('{}Você obteve media de {:.1f} e foi aprovado, PARABENS!{}'.format('\033[1;32m', media, cores['padrao']))

elif 5 <= media < 7:
    print('{}Você obteve media de {:.1f} e foi para recuperação, se esforce!'.format('\033[1;34m', media, cores['padrao']))
