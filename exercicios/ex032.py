# Desafio 32

ano = input('Digite um ano para saber se ele é bissexto: ')
ano_int = int(ano)

if ano_int % 4 == 0 and ano_int % 100 != 0 or ano_int % 400 == 0:
    print(f'O ano {ano_int} é bissexto')
else:
    print(f'O ano {ano_int} não é bissexto')