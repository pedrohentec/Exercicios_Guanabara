# Desafio 40

nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')

if media < 5.0:
    print('REPROVADO')
elif media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')