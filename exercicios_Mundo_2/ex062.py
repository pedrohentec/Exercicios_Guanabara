# Desafio 62

termo  = int(input('Digite o primeiro TERMO: ')) # Inicio
razao = int(input('Digite a razão da P.A: ')) # Salto
quantidade_primeiros = termo + (10 - 1) * razao # Dez primeiros
mais_termos = 'S'
copy_termo = termo

while mais_termos == 'S':
    while copy_termo < quantidade_primeiros +1:
        print(copy_termo, end=' → ')
        copy_termo += razao
    print('Verificação')
    mais_termos = input('Você deseja mostrar mais alguns termos? [S/N]').upper()
    if mais_termos == 'S':
            quantidade_termos = int(input('Quantos? '))
            quantidade_primeiros = quantidade_primeiros + quantidade_termos * razao
            copy_termo = termo
    elif mais_termos == 'N':
        print('Encerrando...')
    else:
        print('Comando invalido')
