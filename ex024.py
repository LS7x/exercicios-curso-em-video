cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('A sua cidade começa com Santo?: {} '.format(cidade[:5].upper() == 'SANTO'))
