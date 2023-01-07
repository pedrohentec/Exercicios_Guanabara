# Desafio 28
from random import randint

programa = randint(0 ,5)
chute = int(input('Chute um número: '))
print('-'*20)
print(f'Número escolhido pelo computador foi {programa}')
print(f'Seu número foi {chute}')
print('-'*20)
if chute == programa:
    print('Você ganhou!')
else:
    print('Você perdeu!')
