# Desafio 39
from datetime import datetime

ano_nascimento = int(input('Qual é o seu ano de nascimento? '))
idade = datetime.now().year - ano_nascimento
print('-='*20)
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar!')
    diferenca = 18 - idade
    ano_alistamento = ano_nascimento + 18
    print(f'Ainda faltam {diferenca} anos para você se alistar!')
    print(f'Seu alistamento será em {ano_alistamento}')
elif idade == 18:
    print('Está na hora de se alistar ao serviço militar!')
else:
    diferenca = idade - 18
    print(f'Já se passaram {diferenca} anos do momento que você deveria se alistar!')
    ano_alistamento = datetime.now().year - diferenca
    print(f'Você deveria ter se alistado em {ano_alistamento}')
    