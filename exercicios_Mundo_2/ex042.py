# Desafio 42

print('Cite 3 retas para ver se é possível formar um triângulo e qual o tipo dele')
reta1 = float(input('Qual é a primeira reta: ').replace(',', '.'))
reta2 = float(input('Qual é a segunda reta: ').replace(',', '.'))
reta3 = float(input('Qual é a terceira reta: ').replace(',', '.'))

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print('As retas citadas, podem formar um triângulo')
    if reta1 == reta2 == reta3: # Se todos os lados são iguais
        print('O formato deste triângulo é EQUILÁTERO')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3: # Se ao menos dois lados são iguais
        print('O formato deste triângulo é ISÓSCELES')
    else: # Se todos os lados são diferentes
        print('O formato deste triângulo é ESCALENO')
else:
    print('Não é possivel fazer um triângulo com as retas citadas')
