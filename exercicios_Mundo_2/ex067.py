# Desafio 67
print('-=' * 20)
print(f'{"T A B U A D A":^40}')
print('-=' * 20)

while True:
    num = int(input('Digite um número para ver sua Tabuada. Para encerrar digite um número negativo.\n'))
    print('-=' * 20)
    contador = 1
    if num < 0:
        print('Encerrando...')
        break
    while contador <= 10:
        multiplicacao = contador * num
        print(f'{num} x {contador:>2} = {multiplicacao}')
        contador += 1