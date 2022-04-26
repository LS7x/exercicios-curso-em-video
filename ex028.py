import random
import time

print('\nIrei pensar em um número de 0 a 5!')
numero = int(input('Tente adivinhar qual número eu pensei: '))

escolhido = random.randint(0, 5)
print('Aguarde estou pensando...')
time.sleep(3)
print('\nO numero escolhido foi: {}'.format(escolhido))

if numero == escolhido:
    print('Parabens!!! Você acertou.')
else:
    print('Que triste :( você errou')
