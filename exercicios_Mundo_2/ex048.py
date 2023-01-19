# Desafio 48
soma_impar = 0

for num in range(1, 501):
   if num % 2 != 0 and num % 3 == 0:
        soma_impar += num 
print(f'A soma entre todos os números ímpares de 1 a 500 é {soma_impar}')
