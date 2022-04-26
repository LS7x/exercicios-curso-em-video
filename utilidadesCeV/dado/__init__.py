from PythonExercicios.utilidadesCeV import moeda


def leiaDinheiro(string):
    while True:
        valor = str(input(string).strip())

        if valor.isalpha() or valor == '':
            print('{}O valor "{}" não é um valor valido!{}'.format('\033[1;31m', valor, '\033[m'))
            moeda.deco(56)

        else:
            valorMod = valor.replace(',', '.')
            return float(valorMod)
