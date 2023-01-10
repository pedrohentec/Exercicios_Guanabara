# Desafio 36
print('SIMULAÇÃO   DE   EMPRÉSTIMO   PEDRO FINANCEIRA')
print('-=' * 30)

valor_casa = input('Qual o valor da casa que deseja comprar? R$')
valor_casa_float = float(valor_casa)
salario = input('Qual o valor do seu salário atual? R$')
salario_float = float(salario)
ano = input('Qual a quantidade de anos que deseja pagar? ')
ano_int = int(ano)
meses = ano_int * 12
porcentagem = salario_float * 30 / 100
prestacao = valor_casa_float / meses
print('-=' * 30)

if prestacao <= porcentagem:
    print('Parabéns seu empréstimo foi APROVADO!')
    print(f'O valor que você pagará por mês será de R${prestacao:.2f}.')
else:
    print('Infelizmente, o resultado da sua simulação foi NEGADO!')
    print('Tente novamente daqui a 6 meses!')
print('-=' * 30)
print('Tenha um bom dia')