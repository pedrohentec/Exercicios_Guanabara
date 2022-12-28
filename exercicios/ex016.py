# Quebrando um número
from math import trunc

num = input('Digite um número real: ')
num_float = float(num)
print(f'O número {num} tem a parte inteira {trunc(num_float)}')