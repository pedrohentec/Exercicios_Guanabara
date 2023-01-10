# Desafio 38 

num1 = input('Digite o primeiro número: ')
num1_int = int(num1)
num2 = input('Digite o segundo número: ')
num2_int = int(num2)
print('-' * 20)
print(f'O primeiro valor é {num1_int}\nO segundo valor é {num2_int}')
print('-' * 20)

if num1_int > num2_int:
    maior = num1_int
    menor = num2_int
elif num2_int > num1_int:
    maior = num2_int
    menor = num1_int

if num1_int == num2_int:
    print('Não existe valor maior ou menor, os dois são iguais')
else:
    print(f'O valor {maior} é o maior')
    print(f'O valor {menor} é o menor')
