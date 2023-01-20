# Desafio 51

termo  = int(input('Digite o primeiro TERMO: '))
razao = int(input('Digite a razão da P.A: '))
dez_primeiros = termo + (10 - 1) * razao # Feita através da resolução com o Guanabara

for pa in range(termo, dez_primeiros + razao, razao):
    print(pa, end=' → ')
print('FIM')

