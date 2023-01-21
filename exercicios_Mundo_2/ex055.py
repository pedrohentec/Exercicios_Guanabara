# Desafio 55
lista_pesos = []

for p in range(1, 6):
    peso_user = float(input(f'Qual peso da {p}° pessoa: ').replace(',', '.'))
    lista_pesos.append(peso_user)

peso_maior = peso_user
peso_menor = peso_user

for peso in lista_pesos:
    if peso >= peso_maior:
        peso_maior = peso
    elif peso_menor >= peso:
        peso_menor = peso


print(f'O maior peso foi {peso_maior} e o menor peso foi {peso_menor}.')