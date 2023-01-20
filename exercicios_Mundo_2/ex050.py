# Desafio 50
pairs = 0
nums_list = []

for nums in range(6):
    value = int(input('Digite um número: '))
    if value % 2 == 0:
        nums_list.append(value)
        pairs += value

print(f'Os valores pares digitados são {",".join(map(str, nums_list))} e a soma entre eles é {pairs}')