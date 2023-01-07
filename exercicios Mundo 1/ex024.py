# Verificando as primeiras letras de um texto

cidade = input('Digite o nome da sua cidade: ').upper()
cidade = cidade.split()
verificacao = 'SANTO' in cidade[0]

print(verificacao)