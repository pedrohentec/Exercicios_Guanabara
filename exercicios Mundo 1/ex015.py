#Aluguel de Carros
dias = input('Quantos dias alugados? ')
dias_int = int(dias)
km_rodados = input('Quantos KM rodados? ')
km_rodados_float = float(km_rodados)
total_dias = dias_int * 60.00
total_km_rodados = km_rodados_float * 0.15
total_servico = total_dias + total_km_rodados

print(f'O total a pagar é de R${total_servico:.2f}')
