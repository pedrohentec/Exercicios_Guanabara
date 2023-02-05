# Desafio 69
pessoas_mais_18 = homens = mulheres_menor_20 = 0

while True:
    print('-=' * 10)
    print(f'CADASTRE UMA PESSOA')
    print('-=' * 10)      
    idade = int(input('Digite a idade: '))
    sexo = pergunta = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo [M/F]: ').upper()

    if idade > 18:
        pessoas_mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('Você deseja continuar? [S/N] ').upper()
    if pergunta == 'S':
        print('-=' * 10)
        print('Reiniciando...')
    elif pergunta == 'N':
        print('-=' * 10)
        print('Encerrando...')
        break
    
if pessoas_mais_18 == 1:
    print(f'{pessoas_mais_18} pessoa tem mais de 18 anos.')
else:
    print(f'{pessoas_mais_18} pessoas tem mais de 18 anos.')

if homens == 1:
    print(f'Apenas {homens} homem foi cadastrado.')
else:
    print(f'{homens} foram cadastrados.')

if mulheres_menor_20 == 1:
    print(f'Apenas {mulheres_menor_20} mulher com menos de 20 anos foi cadastrada.')
else:
    print(f'{mulheres_menor_20} mulheres com menos de 20 anos foram cadastradas.')
