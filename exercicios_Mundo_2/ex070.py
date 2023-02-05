# Desafio 70
produto_barato = produtos_1000 = total = 0
produto_barato_nome = ''

while True:
    nome = input('Nome do produto: ').capitalize()
    preco = float(input(f'Preço de {nome} R$ ').replace(',', '.'))
    # Total de gastos
    total += preco 
    
    # Produtos acima de R$ 1.000,00
    if preco > 1000: 
        produtos_1000 += 1

    # Produto mais barato
    if produto_barato == 0 or preco < produto_barato:
        produto_barato_nome = nome
        produto_barato = preco
    print('-=' * 15)
    
    pergunta = ''
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('Deseja continuar? [S/N] ').strip().upper()[0]
        print('-=' * 15)
    if pergunta == 'N':
        break

print(f'Valor total gasto: R${total:.2f}')
print(f'Produtos acima de R$ 1.000: {produtos_1000}')
print(f'Produto mais barato: {produto_barato_nome} valor de R$ {produto_barato:.2f}')
