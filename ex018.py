from math import sin, cos, tan, radians

angulo = int(input('Digite o valor do ângulo: '))
# O valor do grau está em centígrados (Temperatura etc.), necessario conversão para radianos (Unidade de medida)!
radiano = radians(angulo)

print('O ângulo digitado é de: {}º'.format(angulo))
print('O valor do seno desse ângulo é de: {:.2f}'.format(sin(radiano)))
print('O valor do cosseno desse ângulo é de: {:.2f}'.format(cos(radiano)))
print('O valor da tangente desse ângulo é de: {:.2f}'.format(tan(radiano)))
