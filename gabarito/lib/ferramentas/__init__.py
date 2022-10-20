from paleta import *


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print(f'\n{vermelho}Usuário preferiu não informar um valor!{limpar}')
            return 0
        except:
            print(f'{vermelho}ERRO: Digite um valor inteiro válido!{limpar}')
        else:
            return num


def zeroAEsquerda(num):
    return num if num >= 10 else f'0{num}'
