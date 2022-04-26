from time import sleep

print('{}-{}'.format('\033[1;36m', '\033[m')*60)
print('{}Seja bem vindo, caro amigo!\n'
      'Este é o teste de racicionio do python!{}'.format('\033[1m', '\033[m'))
print('{}-{}'.format('\033[1;36m', '\033[m')*60)

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

print('{}Efetuando calculos...{}\n'.format('\033[1;32m', '\033[m'))
sleep(3)

if n1 > n2:
    print('O {}primeiro{} valor é maior!'.format('\033[1m', '\033[m'))

elif n2 > n1:
    print('O {}segundo{} valor é maior!'.format('\033[1m', '\033[m'))

elif n1 == n2:
    print('{}Os dois valores são iguais!{}'.format('\033[34m', '\033[m'))
