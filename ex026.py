frase = str(input('Digite sua frase: ')).strip().upper()
print('Na sua frase aparece {} letras A!'.format(frase.count('A')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição: {}'.format(frase.rfind('A')+1))
