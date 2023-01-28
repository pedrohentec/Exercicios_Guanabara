# Desafio 57
sexo = input('Qual o seu sexo? [M/F] ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dado incorreto.\nQual o seu sexo? [M/F] ').upper()
print('FIM')
