# Conversor de Moedas (utilizando valor do dolar atual (27/12/2022))

dinheiro_carteira = input('Quanto dinheiro você tem na sua carteira? R$')
dinheiro_carteira_float = float(dinheiro_carteira)
print('---------------------------------------------------')
# Dolar
dolar = 5.29
poder_de_compra = dinheiro_carteira_float / dolar
print(f'Com R${dinheiro_carteira_float} você pode comprar US${poder_de_compra:.2f}')

print('---------------------------------------------------')
#Euro
euro = 5.63
poder_de_compra = dinheiro_carteira_float / euro
print(f'Com R${dinheiro_carteira_float} você pode comprar €{poder_de_compra:.2f}')

print('---------------------------------------------------')
#Libra Esterlina
libra = 6.36
poder_de_compra = dinheiro_carteira_float / libra
print(f'Com R${dinheiro_carteira_float} você pode comprar £{poder_de_compra:.2f}')

print('---------------------------------------------------')
#Peso Argentino
peso_argentino = 0.030
poder_de_compra = dinheiro_carteira_float / peso_argentino
print(f'Com R${dinheiro_carteira_float} você pode comprar ARS {poder_de_compra:.2f}')

print('---------------------------------------------------')
#Iene
iene = 0.040
poder_de_compra = dinheiro_carteira_float / iene
print(f'Com R${dinheiro_carteira_float} você pode comprar ¥{poder_de_compra:.2f}')