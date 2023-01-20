# Desafio 52

num = int(input('Digite um número e veja se é primo ou não: '))

for n in range(2, num):
    if num % n == 0:
        print(f'O {num} não é um número primo')
        break
else:
    print(f'O {num} é um número primo')

#f'O {num} é um número primo'
#f'O {num} não é um número primo'