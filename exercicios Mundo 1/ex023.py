# Separando dígitos de um número

# Forma como eu fiz:
num = input('Digite um numero: ')
lista = num.split()

print(f'Unidade: {lista[0][3]}')
print(f'Dezena: {lista[0][2]}')
print(f'Centena: {lista[0][1]}')
print(f'Milhar: {lista[0][0]}')

# Após correção na aula:

num = input('Digite um numero: ')
num_int = int(num)
u = num_int // 1 % 10
d = num_int // 10 % 10
c = num_int // 100 % 10
m = num_int // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')