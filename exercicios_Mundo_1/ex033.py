# Desafio 33

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num3 = input('Digite o terceiro número: ')
num1_float = float(num1)
num2_float = float(num2)
num3_float = float(num3)

if num1_float > num2_float and num1_float > num3_float:
    print(f'O número {num1_float} é o maior!')
elif num2_float > num1_float and num2_float > num3_float:
    print(f'O número {num2_float} é o maior!')
else:
    print(f'O número {num3_float} é o maior!')

if num1_float < num2_float and num1_float < num3_float:
    print(f'O número {num1_float} é o menor!')
elif num2_float < num1_float and num2_float < num3_float:
    print(f'O número {num2_float} é o menor!')
else:
    print(f'O número {num3_float} é o menor!')
