# Desafio 44

preco = float(input('Qual o preço do produto? R$').replace(',', '.'))
pagamento = input('Qual será a sua forma de pagamento?\n1-Dinheiro/Cheque\n2-Cartão de Crédito\n')

if pagamento == '1': # Pagamento em Dinheiro/Cheque
    print('Nessa forma de pagamento você terá um desconto de 10% no valor da compra.')
    desconto = preco - (preco * 10 / 100)
    print(f'Você irá pagar R${desconto:.2f} ao final da compra')
elif pagamento == '2': # Cartão
    pagamento_cartao = input('Vai ser à vista ou parcelado?\n1-À Vista\n2-Parcelado\n')
    if pagamento_cartao == '1':
        print('Nessa forma de pagamento você terá um desconto de 5% no valor da compra.')
        desconto = preco - (preco * 5 / 100)
        print(f'Você irá pagar R${desconto:.2f} ao final da compra')
    else:
        parcelado_cartao = int(input('Deseja pagar em quantas vezes? '))
        if parcelado_cartao <= 2:
            print(f'Você irá pagar R${preco:.2f} ao final da compra')
        else:
            print('Nessa forma de pagamento você terá um acréscimo de 20% de juros')
            juros = preco + (preco * 20 / 100)
            print(f'Você irá pagar R${juros:.2f} ao final da compra')
else:
    print('Você não digitou uma opção válida')
