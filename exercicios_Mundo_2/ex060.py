# Desafio 60
num = int(input('Digite um número para ver o seu fatorial: '))

resultado = 1
inicio = ''

# Usando for
for n in range(num, 0, -1):
    resultado *= n
    if n == 1:
        inicio += (f'{n}=')
    else:
        inicio += (f'{n}x') 

print(f'{inicio}{resultado}')

# Usando while
while num > 0:
    resultado *= num
    if num == 1:
        inicio += (f'{num}=')
    else:
        inicio += (f'{num}x') 
    num -= 1

print(f'{inicio}{resultado}')