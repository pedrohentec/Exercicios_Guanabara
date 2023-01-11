# Desafio 43

print('BALANÇA DO PEDRÃO')
print('-='*20)
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: ').replace(',', '.'))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obsidade')
else:
    print('Obesidade mórbida')
