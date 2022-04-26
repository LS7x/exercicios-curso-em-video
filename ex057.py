from time import sleep

cores = {'padrao':'\033[m',
         'vermelho':'\033[1;31m'}

print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)
print('{}Efetuando validação de dados!'.format('\033[1m').center(60))
print('{}-{}'.format(cores['vermelho'], cores['padrao'])*60)

sexo = 'A'

while sexo not in 'MmFf':
    print('{}Utilize a regra a seguir:'
          '\n[M] Masculino'
          '\n[F] Feminino\n'.format('\033[1m'))
    sexo = str(input('Digite o seu sexo: ')).upper().strip()

    if sexo not in 'MmFf':
        print('{}Opção invalida, tente novamente!{}'.format(cores['vermelho'], cores['padrao']))
        print('{}-{}'.format(cores['vermelho'], cores['padrao']) * 60)
        sleep(1)

print('{}Dados validados!{}'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['vermelho'], cores['padrao']) * 60)
