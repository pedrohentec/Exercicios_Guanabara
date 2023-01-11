preco = float(input('Qual o preço do produto? R$').replace(',', '.'))
pagamento = input('''Qual será a sua forma de pagamento?
1-à vista no Dinheiro/Cheque
2-à vista no Cartão de Crédito
3-2x no Cartão de Crédito
4-3x ou mais no Cartão de Crédito
''')
if pagamento == '1':
    desconto = preco - (preco * 10 / 100)
    print(f'Você tem um desconto de 10%, sendo assim irá pagar R${desconto:.2f} ao final da compra')
elif pagamento == '2':
    desconto = preco - (preco * 5 / 100)
    print(f'Você tem um desconto de 5%, sendo assim irá pagar R${desconto:.2f} ao final da compra')
elif pagamento == '3':
    preco_parcelas = preco / 2
    print(f'Você irá pagar R${preco:.2f} em 2 parcelas de R${preco_parcelas:.2f} ao final da compra')
elif pagamento == '4':
    juros = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    preco_parcelas = preco / parcelas
    print(f'Você terá um acréscimo 20% de juros, sendo assim irá pagar R${juros:.2f} em {parcelas} parcelas de R${preco_parcelas:.2f} ao final da compra')
else:
    print('Você não digitou uma opção válida')
