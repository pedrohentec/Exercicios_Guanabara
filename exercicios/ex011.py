#Pintando uma Parede
largura = input('Largura da parede: ')
largura_float = float(largura)
altura = input('Altura da parede: ')
altura_float = float(altura)
area = largura_float * altura_float
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura_float}x{altura_float} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
