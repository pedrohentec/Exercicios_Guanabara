# Desafio 58
from random import randint
chutes = 1

num_user = int(input('Chute o número em que a máquina esta pensando de 0 a 10: '))
maquina = randint(0,10)

while num_user != maquina:
    chutes += 1
    print('Você errou!')
    num_user = int(input('Chute novamente um número de  0 a 10: '))
else:
    print('Você acertou!')

if chutes > 1:
    print(f'Foram necessários {chutes} chutes para conseguir acertar!')
else:
    print(f'Foi necessário apenas {chutes} chute para conseguir acertar!')