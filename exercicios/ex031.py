# Desafio 31

distancia = input('Qual a distância da viagem em KM? ').replace(',', '.')
distancia_float = float(distancia)

if distancia_float <= 200:
    preco_passagem = (distancia_float * 0.50)
else:
    preco_passagem = (distancia_float * 0.45)
    
print(f'O preço da passagem é {preco_passagem:.2f}')
