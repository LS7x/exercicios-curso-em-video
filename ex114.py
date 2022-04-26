import urllib
import urllib.request
import urllib.error

cores = {'padrao': '\033[m', 'negrito': '\033[1m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}


def verificar():
    try:
        site = urllib.request.urlopen('http://www.pudim.com.br/')

    except urllib.error.URLError:
        print(f'{cores["vermelho"]}O site pudim não esta acessivel no momento!{cores["padrao"]}')

    else:
        print(f'{cores["verde"]}O site pudim esta acessivel no momento!{cores["padrao"]}')


verificar()
