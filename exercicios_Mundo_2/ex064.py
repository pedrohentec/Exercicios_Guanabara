# Desafio 64
import os
user = 0
nums = []
soma = 0

while user != 999:
    user = int(input('Digite um número (Caso queira parar, digite 999): '))
    os.system('cls')
    if user != 999:
        nums.append(user)
        soma += user

print(f'Foram digitados {len(nums)} números e a soma entre eles é {soma}')
