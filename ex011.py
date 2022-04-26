largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print('A largura digitada é de: {}m²'.format(largura))
print('A altura digitada é de: {}m²'.format(altura))
print('O valor da area do local é de: {}m²'. format(area))
print('A quantidade necessaria de tinta é de: {}l'.format(tinta))
