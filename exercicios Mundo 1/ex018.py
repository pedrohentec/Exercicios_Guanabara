# Seno, Cosseno e Tangente de um ângulo

from math import sin, tan, cos, radians

angulo = input('Digite o valor do ângulo: ')
angulo_float = float(angulo)
radiano = radians(angulo_float)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'O ângulo de {angulo}° tem os seguintes valores:')
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
