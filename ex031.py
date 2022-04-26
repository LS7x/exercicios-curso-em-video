import time

print('''\nSeja bem vindo a Air Python viagens!
Asseguir iremos calcular o valor da sua viagem!\n''')

distancia = float(input('Digite a distancia da viagem em KM: '))
print('Aguarde, calculando valor...\n')
time.sleep(3)

if distancia <= 200:
    curta = distancia * 0.50
    print('O valor da sua viagem saira entorno de: R${:.2f}'.format(curta))

if distancia > 200:
    longa = distancia * 0.45
    print('O valor da sua viagem com desconto saira entorno de: RS{:.2f}'.format(longa))

print('Tenha uma boa viagem!')
