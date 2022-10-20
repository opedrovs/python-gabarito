from lib.menu import *
from lib.ferramentas import *


gabarito = list()

while True:
    cabecalho('CADASTRE O GABARITO')
    for cont in range(1, 11):
        while True:
            altern = input(f'Alternativa da {zeroAEsquerda(cont)}ª questão: ').strip().upper()
            if altern == 'A' or altern == 'B' or altern == 'C' or altern == 'D' or altern == 'E':
                break
            print(f'{vermelho}ERRO: Digite uma alternativa válida entre A e E!{limpar}')
        gabarito.append(altern)

    while True:
        linha()
        for pos, alternativa in enumerate(gabarito):
            print(f'{zeroAEsquerda(pos + 1)}º - {alternativa}')

        resp = input('O gabarito está da forma que deseja? [S/N] ').strip().upper()
        if resp == 'S' or resp == 'N':
            break
        print(f'{vermelho}ERRO: Digite apenas S ou N.{limpar}')
    if resp == 'S':
        break
    gabarito.clear()

acertos = list()
alunos = list()
ficha = dict()
codAluno = 1

while True:
    cabecalho(f'CADASTRAR {codAluno}ª ALUNO')
    while True:
        nome = input('Nome completo do aluno: ')
        if len(nome) != 0:
            ficha['nome'] = nome
            break
        print(f'{vermelho}ERRO: Digite um nome completo válido!{limpar}')

    for cont in range(1, 11):
        while True:
            altern = input(f'Alternativa da {zeroAEsquerda(cont)}ª questão: ').strip().upper()
            if altern == 'A' or altern == 'B' or altern == 'C' or altern == 'D' or altern == 'E':
                break
            print(f'{vermelho}ERRO: Digite uma alternativa válida entre A e E!{limpar}')

        if altern == gabarito[cont - 1]:
            acertos.append(1)
        else:
            acertos.append(0)
    ficha['acertos'] = acertos[:]
    ficha['nota'] = sum(acertos[:])
    alunos.append(ficha.copy())
    acertos.clear()
    ficha.clear()

    while True:
        resp = input('Deseja continuar? [S/N] ').strip().upper()
        if resp == 'S' or resp == 'N':
            break
        print(f'{vermelho}ERRO: Responda apenas S ou N.{limpar}')
    if resp == 'N':
        break
    codAluno += 1
linha()

total = maior = menor = 0
for pos, aluno in enumerate(alunos):
    total += sum(aluno['acertos'])
    if pos == 0:
        maior = aluno['nota']
        menor = aluno['nota']
    else:
        if aluno['nota'] > maior:
            maior = aluno['nota']
        if aluno['nota'] < menor:
            menor = aluno['nota']

print(f'Média das Notas da Turma: {total / codAluno}.')
print(f'Total de alunos que fizeram a prova: {codAluno}.')

print(f'Maior nota foi {maior}, tiraram os alunos: ', end='')
for pos, aluno in enumerate(alunos):
    if aluno['nota'] >= maior:
        print(f'{aluno["nome"]}', end='')
        print('. ' if pos < len(alunos) else ', ', end='')
print()

print(f'Menor nota foi {menor}, tiraram os alunos: ', end='')
for pos, aluno in enumerate(alunos):
    if aluno['nota'] <= menor:
        print(f'{aluno["nome"]}', end='')
        print(', ' if pos != len(alunos) - 1 else '. ', end='')
print()
