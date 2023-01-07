# Conversor de Medidas
distancia = input('Digite uma distância em metros: ')
distancia_float = float(distancia)

print(f'''A medida de {distancia_float}m corresponde a

{distancia_float / 1000}Km
{distancia_float / 100}hm
{distancia_float / 10}dam
{distancia_float / 0.1:.0f}dm
{distancia_float / 0.01:.0f}cm
{distancia_float / 0.001:.0f}mm
''')