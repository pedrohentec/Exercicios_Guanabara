# Calculando Descontos
salario_funcionario = input('Qual é o salário do funcionário? R$')
salario_funcionario_float = float(salario_funcionario)
aumento = salario_funcionario_float + (salario_funcionario_float * 15 / 100)
print(f'Um funcionário que ganhava R${salario_funcionario_float:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}.')