# Desafio 54
from datetime import datetime
anos_nascimento = []
maiores = 0
menores = 0


for i in range(1,8):
    ano_nascimento = int(input(f'Qual o ano de nascimento da {i}° pessoa: '))
    anos_nascimento.append(ano_nascimento)

for ano in anos_nascimento:
    idade_atual = datetime.now().year - ano
    if idade_atual >= 18:
        maiores += 1
    else:
        menores += 1
        
print(f'{maiores} já atingiram a maioridadde\n{menores} ainda não atingiram a maioridade')