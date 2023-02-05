# Desafio 71

print('BANCO DO PEDRÃO')
valor_a_sacar = int(input('Que valor você quer sacar? R$ '))

# Caixa possui as cédulas de R$ 50 // R$ 20 // R$ 10 // R$ 1

nota50 = valor_a_sacar // 50
valor_a_sacar = valor_a_sacar % 50

nota20 = valor_a_sacar // 20
valor_a_sacar = valor_a_sacar % 20

nota10 = valor_a_sacar // 10
valor_a_sacar = valor_a_sacar % 10

nota1 = valor_a_sacar // 1

print(f'''
Quantidade de notas de R$ 50,00 ➜  {nota50}
Quantidade de notas de R$ 20,00 ➜  {nota20}
Quantidade de notas de R$ 10,00 ➜  {nota10}
Quantidade de notas de R$ 1,00 ➜  {nota1}
''')