# Desafio 29
print('-'*15)
velocidade = input('Qual a velocidade atual do carro: ')
velocidade_float = float(velocidade)
velocidade_maxima = 80
km_acima = velocidade_float - velocidade_maxima
multa = km_acima * 7
print('-'*15)

if velocidade_float > velocidade_maxima:
    print(f'Você foi multado, por passar {km_acima}Km acima do permitido!')
    print(f'O valor da multa é R${multa:.2f}.')
else:
    print('Boa viagem!')
