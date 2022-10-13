texto = input('Ingrese texto: ')

aux  = ''
i = 0
while i < len(texto):
    if texto[i] == ' ':
        aux = aux + texto[i + 1].upper()
        i = i + 2
    else:
        aux =  aux + texto[i]
        i = i + 1

print(aux)
