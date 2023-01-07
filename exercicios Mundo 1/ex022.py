# 

nome = input('Digite o seu nome completo: ')
nome_list = nome.split()
nome_len = nome.replace(' ','')

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome_len)} letras')
print(f'Seu primeiro nome {len(nome_list[0])} letras')