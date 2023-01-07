# Desafio 35
print('Digite três retas para ver se é possivel formar um triângulo')
print('-'*30)
reta1 = input('Digite a reta 1: ')
reta2 = input('Digite a reta 2: ')
reta3 = input('Digite a reta 3: ')

reta1_float = float(reta1)
reta2_float = float(reta2)
reta3_float = float(reta3)

print('-'*30)

if (reta1_float + reta2_float) > reta3_float and (reta2_float + reta3_float) > reta1_float and (reta3_float + reta1_float) > reta2_float:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')
