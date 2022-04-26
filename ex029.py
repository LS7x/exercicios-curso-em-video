import time

print('\nSeja bem vindo ao calculador de multa!')
print('Nesse programa sera demonstrado se o veiculo ultrapassou a velocidade permitida\n')

velocidade = int(input('Qual era a velocidade do veiculo: '))

if velocidade > 80:
      print('\nO veiculo ultrapassou a velocidade permitida de 80Km/h!')
      velocidade = velocidade - 80
      multa = velocidade * 7
      print('Processando valor da multa...\n')
      time.sleep(3)
      print('Aplicar a multa no valor a seguir: R${}'.format(multa))

else:
      print('O veiculo trafegou na velocidade permitida!')
