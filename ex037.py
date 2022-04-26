from time import sleep
print('{}-{}'.format('\033[36m', '\033[m')*60)
print('{}Seja bem-vindo ao conversor python'
      '\nAsseguir iremos efetuar as conversoes da base numerica !{}'.format('\033[1m', '\033[m'))
print('{}-{}'.format('\033[36m', '\033[m')*60)

numero = int(input('Digite o seu numero inteiro: '))

print('\n{}Bom agora vamos para conversão!'
      '\nSiga a lista abaixo para saber em qual converter:{}\n'
      '\nPara conversão para {}binario{} digite 1'
      '\nPara conversão para {}octal{} digite 2'
      '\nPara conversão para {}hexadecimal{} digite 3\n'.format('\033[1m', '\033[m', '\033[1;33m', '\033[m', '\033[1;33m', '\033[m', '\033[1;33m', '\033[m'))

conversao = int(input('Digite o valor para conversão: '))
print('Aguarde efetuando conversão...\n')
sleep(3)

if conversao == 1:
    binario = bin(numero)[2:]
    print('{}O valor {} convertido para binario sera: {}{}'.format('\033[32m', numero, binario, '\033[m'))

elif conversao == 2:
    octal = oct(numero)[2:]
    print('{}O valor {} convertido para octal sera: {}{}'.format('\033[32m', numero, octal, '\033[m'))

elif conversao == 3:
    hexa = hex(numero)[2:]
    print('{}O valor {} convertido para hexadecimal sera: {}{}'.format('\033[32m', numero, hexa, '\033[m'))

else:
    print('{}Conversão invalida{}'.format('\033[1;31m', '\033[m'))
