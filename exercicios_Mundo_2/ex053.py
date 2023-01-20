# Desafio 53 
frase = input('frase: ').replace(" ", "").upper()
inverso = frase[::-1]
print(f'{frase}. Ao contrario seria: {inverso}')

if frase == inverso:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase não é um Palíndromo')
