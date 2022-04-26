from time import sleep

cores = {'padrao':'\033[m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)
print('{}Seja bem vindo a contagem de fogos de artificios!{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)

print('Você esta preparado?')
input('')

for fogos in range(10, 0-1, -1):
    print('{}{}!{}'.format(cores['vermelho'], fogos, cores['padrao']))
    sleep(1)
print('{}\nKABUM !!!{}'.format(cores['vermelho'], cores['padrao']))
