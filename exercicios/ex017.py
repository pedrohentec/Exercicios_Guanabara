# Calculo de comprimento da hipotenusa

from math import hypot
comprimento_oposto = input('Digite o valor do cateto oposto: ')
comprimento_oposto_float = float(comprimento_oposto)
comprimento_adjacente = input('Digite o valor do cateto adjacente: ')
comprimento_adjacente_float = float(comprimento_adjacente)
hipotenusa = hypot(comprimento_oposto_float, comprimento_adjacente_float)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')