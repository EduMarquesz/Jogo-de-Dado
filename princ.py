from random import randint
from time import sleep
from defs.fun import *
lista = list()
titulo('Jogar Dado')
try:
    lista.append(int(input('Número mínimo: ')))
    lista.append(int(input('Número máximo: ')))
    v = randint(lista[0], lista[1])
    print('Analisando Resultado...')
    sleep(2)
    print(f'valor sorteado: {v}')
except ValueError:
    print('\033[31mNÚMERO INVÁLIDO!\033[m')
except KeyboardInterrupt:
    print('\033[31mUSUÁRIO INTERROMPEU O PROGRAMA.\033[m')
