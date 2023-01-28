# Desfio 61

termo  = int(input('Digite o primeiro TERMO: '))
razao = int(input('Digite a razão da P.A: '))
dez_primeiros = termo + (10 - 1) * razao

while termo < dez_primeiros+1:
    print(termo, end=' → ')
    termo += razao
print('FIM')