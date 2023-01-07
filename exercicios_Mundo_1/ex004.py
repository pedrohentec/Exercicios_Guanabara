# Dissecando uma variável

algo = input('Digite algo: ')
tipo = type(algo)
print('------------------------------------------')
print(f'O tipo primitivo desse valor é {tipo}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumério? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')
print('------------------------------------------')

