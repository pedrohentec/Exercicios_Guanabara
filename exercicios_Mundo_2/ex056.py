# Desafio 56
pessoas = 0
media_idade = 0
homem_mais_velho = 0
mulheres_menos_20anos = 0

print('-' * 20)
for d in range(4):
  pessoas += 1
  print(f'{pessoas}° PESSOA')
  print('-' * 20)
  nome = input('Qual seu nome? ').capitalize()
  idade = int(input(f'Qual a sua idade {nome}? '))
  sexo = input('Sexo Masculino ou Feminino? [M/F]').upper()
  print('-' * 20)
  media_idade += idade
  if sexo == 'M': # Caso seja Masculino faz a condição do homem mais velho e nome do mesmo
    if idade > homem_mais_velho:
      homem_mais_velho = idade
      nome_homem_mais_Velho = nome
  else: # Caso seja Feminino, faz a condição de mulher com menos de 20 anos e soma a quantidade
    if idade < 20:
      mulheres_menos_20anos += 1

media_idade = media_idade / pessoas # Média do grupo
print(f'A idade média do grupo é {media_idade} anos.\nO homem mais velho é {nome_homem_mais_Velho} com a idade de {homem_mais_velho} anos.')

if mulheres_menos_20anos > 1: # Condição criada para caso seja apenas 1 mulher ou mais de 1 sendo mulheres
  print(f'Dentro do grupo tem {mulheres_menos_20anos} mulheres com menos de 20 anos.')
else:
  print(f'Dentro do grupo tem {mulheres_menos_20anos} mulher com menos de 20 anos.')