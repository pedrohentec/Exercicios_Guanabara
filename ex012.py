# Calculando Descontos
preco_produto = input('Qual preço do produto? R$')
preco_produto_float = float(preco_produto)
desconto = preco_produto_float - (preco_produto_float * 5 / 100)
print(f'O produto que custava R${preco_produto_float:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}.')
