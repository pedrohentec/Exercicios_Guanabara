# Desafio 59
opcao = ''
print('-=' * 15)
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))

while opcao != '5':
    print('-=' * 15)
    opcao = input('''     M      E      N     U
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa\n''')
    print('-=' * 15)
    if opcao == '1':
        soma = v1 + v2
        print(f'{v1:.2f} + {v2:.2f} é {soma:.2f}')
    elif opcao == '2':
        multiplicacao = v1 * v2
        print(f'{v1:.2f} X {v2:.2f} é {multiplicacao:.2f}')
    elif opcao == '3':
        if v1 == v2:
            print(f'Os números {v1} e {v2} são iguais')
        elif v1 > v2:        
            print(f'O maior valor é {v1}')
        else:
            print(f'O maior valor é {v2}')
    elif opcao == '4':
        print('Reiniciando...')
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif opcao == '5':
        print('Saindo do programa...')
    else:
        print('Comando inválido')