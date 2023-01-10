# Desafio 37

num = input('Digite um número inteiro para fazer a conversão: ')
num_int = int(num)
base_conversao = input('Qual será a base de conversão? \n1 Binário\n2 Octal\n3 Hexadecimal\n')

if base_conversao == '1':
    binario = bin(num_int)
    print(f'O binário de {num_int} é {binario[2:]}')
elif base_conversao == '2':
    octal = oct(num_int)
    print(f'O binário de {num_int} é {octal[2:]}')
elif base_conversao == '3':
    hexadecimal = hex(num_int)
    print(f'O binário de {num_int} é {hexadecimal[2:]}')
else:
    print('Você não digitou uma base de conversão valida! Tente novamente.')