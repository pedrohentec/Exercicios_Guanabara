# Primeira e última ocorrência de uma string

# Com eu fiz:

frase = input('Digite uma frase: ').upper().lstrip()

print(f'A Letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A")}')
print(f'A última letra A apareceu na posição {frase.rfind("A")}')

# Após correção da aula:

frase = input('Digite uma frase: ').upper().strip()

print(f'A Letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A") + 1}')
print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}')