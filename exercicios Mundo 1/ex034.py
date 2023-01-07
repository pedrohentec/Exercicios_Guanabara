# Desafio 34

salario = input('Qual o seu salário? ')
salario_float = float(salario)

if salario_float > 1250.00:
    aumento = (salario_float * 10 / 100) + salario_float
    print(f'O salário de R${salario_float:.2f} recebeu um aumento de 10%, totalizando um valor de R${aumento:.2f}')
else:
    aumento = (salario_float * 15 / 100) + salario_float
    print(f'O salário de R${salario_float:.2f} recebeu um aumento de 15%, totalizando um valor de R${aumento:.2f}')
