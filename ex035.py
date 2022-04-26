cores = {'cinza':'\033[37m',
         'ciano':'\033[36m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'padrao':'\033[m'}

c1 = int(input('Digite o comprimento do {}1º lado:{} '.format(cores['ciano'], cores['padrao'])))
c2 = int(input('Digite o comprimento do {}2º lado:{} '.format(cores['ciano'], cores['padrao'])))
c3 = int(input('Digite o comprimento do {}3º lado:{} '.format(cores['ciano'], cores['padrao'])))

if (c1 + c2 < c3) or (c1 + c3 < c2) or (c2 + c3 < c1):
    print('{}Não é possivel formar um triangulo!{}'.format(cores['vermelho'], cores['padrao']))

else:
    print('{}É possivel formar um triangulo!{}'.format(cores['verde'], cores['padrao']))
