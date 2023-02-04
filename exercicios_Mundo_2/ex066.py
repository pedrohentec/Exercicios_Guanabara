# Desafio 66

contador = soma = 0

while True:
    num = int(input('Digite um número [999 para encerrar]: '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'Foram digitados {contador} números, e a soma entre eles é {soma}.')
