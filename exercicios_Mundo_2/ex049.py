# Desafio 49

print('T  A  B  U  A  D  A')
num_user = int(input('Digite um número de 1 a 10 para ver sua tabuada: '))
print('-=' * 10)
for num in range(0,11):
    total_value = num_user * num
    print(f'{num_user} x {num:>2} = {total_value:>3}')
print('-=' * 10)
