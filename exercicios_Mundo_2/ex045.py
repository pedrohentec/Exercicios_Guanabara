# Desafio 45

from random import choice
print('J O K E N P Ô ')

user = input('Escolha:\nPedra\nPapel\nTesoura\n').capitalize()
options_machine = ['Pedra', 'Papel', 'Tesoura']
machine = choice(options_machine)

if user != 'Pedra' and user != 'Papel' and user != 'Tesoura':
    print('Você não digitou uma opção válida!')
else:
    print('-=' * 20)
    print(f'Você escolheu {user}')
    print(f'A máquina escolheu {machine}')
    print('-=' * 20)   
    if user == machine:
        print('EMPATE!!!')
    else:
        if user == 'Pedra' and machine == 'Tesoura':
            print('Você GANHOU!!!')
        elif user == 'Papel' and machine == 'Pedra':
            print('Você GANHOU!!!')
        elif user == 'Tesoura' and machine == 'Papel':
            print('Você GANHOU!!!')
        else:
            print('Você PERDEU!!!')


    