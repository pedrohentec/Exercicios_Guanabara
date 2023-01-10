# Desafio 41
from datetime import datetime

ano_nascimento = abs(int(input('Qual seu ano de nascimento? ')))
idade = datetime.now().year - ano_nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')