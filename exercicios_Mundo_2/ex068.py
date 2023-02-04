# Desafio 68
from random import randint
vitorias = 0
usuario  = ' '

while True:
    while usuario not in 'PI': 
        usuario = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    num_usuario = int(input('Jogue seu número: '))
    num_maquina = randint(0, 5)
    print('-=' * 10)
    print(f'Seu número foi {num_usuario}')
    print(f'O número da máquina foi: {num_maquina}')
    soma = num_usuario + num_maquina
    if soma % 2 == 0:
        print(f'Total de {soma}. PAR')
    else:
        print(f'Total de {soma}. ÍMPAR')
    print('-=' * 10)

    if usuario == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print(f'Você ganhou!')
        else:
            print(f'Você perdeu!')
            break
    elif usuario == 'I':
        if soma % 2 == 1:
            vitorias += 1
            print(f'Você ganhou!')
        else:
            print(f'Você perdeu!')
            break

print('-=' * 10)
if vitorias == 1:
    print(f'Você teve {vitorias} vitória consecutiva.')
else:
    print(f'Você teve {vitorias} vitórias consecutivas.')
