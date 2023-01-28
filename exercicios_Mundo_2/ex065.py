# # Desafio 65
verificacao = 'S'
media = 0
quantidade_nums = 0
menor = 0
maior = 0

while verificacao == 'S':
    num = int(input('Digite um número: '))
    quantidade_nums += 1
    media += num
    if quantidade_nums == 1:
        maior = menor = num    
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    print('-=' * 15)
    verificacao = input('Deseja continuar? [S/N]').upper()
    if verificacao == 'N':
        print('Encerrando...')

media = media / quantidade_nums
print(f'A media entre os números digitados é {media:.2f}\nO maior foi {maior} e o menor foi {menor}.')
