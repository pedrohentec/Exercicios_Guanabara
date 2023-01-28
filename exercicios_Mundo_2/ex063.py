# Desafio 63

num = int(input('Quantas sequências você quer ver? '))
termo1 = 0
termo2 = 1
print(f'{termo1} ➞  {termo2}', end='')
contador = 3

while num >= contador:
    termo3 = termo1 + termo2
    print(f' ➞  {termo3}', end='')
    contador += 1
    termo1 = termo2
    termo2 = termo3

print(' ➞ FIM')