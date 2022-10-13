def insertar(lista, pos, valor):
    # Solo positivos
    i = 0
    if pos >= len(lista):
        lista.append(valor)
        return lista
    while i < len(lista):
        if pos == i:
            aux = lista[i]
            lista[i] = valor
        if pos < i:
            aux_2 = lista[i]
            lista[i] == aux
            aux_2 = aux
        i = i + 1
    lista.append(aux)
    return lista

def insertar_ez(lista,pos, valor):
    # Solo positivos
    i = 0
    if pos >= len(lista):
        lista.append(valor)
        return lista
    lista_aux = []
    i = 0
    while i < len(lista):
        if i == pos:
            lista_aux.append(valor)
        lista_aux.append(lista[i])
        i = i + 1
    return lista_aux
