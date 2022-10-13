def validar(texto):
    '''Solicita un entero,
        si el entero ingresado es válido lo retorna
        sino, lo pide de nuevo
    '''
    seguir = True
    while seguir:
        valor = input(texto)
        # Si el número es negativo
        aux = valor.split('-')
        if aux[0] == '' and aux[1].isdigit():
            return int(valor)
        # Si el número es positivo con un signo
        aux = valor.split('+')
        if aux[0] == '' and aux[1].isdigit():
            return int(valor)
        if valor.isdigit():
            return int(valor)
        print('Valor incorrecto, ingrese nuevamente')

def encontrar_minimo(lista):
    i = 0
    minimo = lista[0]
    
    while i < len(lista):
        if minimo > lista[i]:
            minimo = lista[i]
        i = i + 1
    return minimo

lista = []

i = 0
while i < 10:
    txt = 'Ingrese el valor ' + str(i + 1) + '°:'
    valor = validar(txt)
    lista.append(valor)
    i = i + 1

print(lista)
minimo = encontrar_minimo(lista)
print(minimo)
