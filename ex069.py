from time import sleep

cores = {'padrao': '\033[m',
         'roxo': '\033[1;35m'}

print('{}-{}'.format(cores['roxo'], cores['padrao']) * 70)
print('{}Seja bem-vindo a pesquisa de campo da Python Company'.format('\033[1m').center(70))
print('Iremos coletar algumas informações e revelar outras informações!{}'.format(cores['padrao']).center(70))
print('{}-{}'.format(cores['roxo'], cores['padrao']) * 70)

print('{}Siga as regras a seguir para informar os dados:{}'
      '\nPara informar a idade, informe um número inteiro!\n'
      '\nPara informar o sexo, utlize:'
      '\n[M] para masculino'
      '\n[F] para feminino\n'
      '\nPara continuar utlize:'
      '\n[S] para sim'
      '\n[N] para não!'.format('\033[1m', cores['padrao']))
print('{}-{}'.format(cores['roxo'], cores['padrao']) * 70)

somaHomens = 0
maisIdade = 0
somaMulheres = 0

while True:
    idade = 0
    while idade <= 0:
        idade = int(input('Informe a idade da pessoa: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo da pessoa: ').strip().upper())

    cadastro = ' '
    while cadastro not in 'SN':
        cadastro = str(input('Deseja continuar: ').strip().upper())

    if idade > 18:
        maisIdade += 1

    if sexo == 'M':
        somaHomens += 1

    if idade < 20 and sexo == 'F':
        somaMulheres += 1

    print('{}-{}'.format(cores['roxo'], cores['padrao']) * 70)
    if cadastro == 'N':
        break

print('Aguarde, organizando...\n')
sleep(3)

print('{}{} Pessoas possuem idade maior que 18 anos.{}'.format(cores['roxo'], maisIdade, cores['padrao']))
print('{}Foram cadastrados {} homens.{}'.format(cores['roxo'], somaHomens, cores['padrao']))
print('{}Possui {} mulheres com idade inferior a 20 anos.{}'.format(cores['roxo'], somaMulheres, cores['padrao']))
