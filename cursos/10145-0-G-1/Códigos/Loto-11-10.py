from random import randint, shuffle

def sortear():
        
    '''
    lista = []

    while len(lista) < 6:
        x = randint(1,45)
        if x not in lista:
            lista.append(x)
    '''
    lista = list(range(1,46))
    shuffle(lista)
    loto = lista[0:6]
    return loto

def validar_entero(texto):

    valor = input(texto)
    i = 0
    if valor[i] in '+-' and len(valor) == 1:
        print('El número ingresado no es valido')
        print('Intente nuevamente')
        return validar_entero(texto)
    if valor[i] not in '+-1234567890':
        print('El número ingresado no es valido')
        print('Intente nuevamente')
        return validar_entero(texto)
    i = 1
    while i < len(valor):
        if valor[i] not in '1234567890':
            print('El número ingresado no es valido')
            print('Intente nuevamente')
            return validar_entero(texto)
        i = i + 1
    valor = int(valor)
    return valor

def pedir_numeros(n):
    i = 0
    numeros = []
    while len(numeros) < n:
        valor = validar_entero('Ingrese un valor: ')
        numeros.append(valor)
    return numeros

def comparar_listas(apuesta, sorteo):
    aciertos = 0
    for e1 in apuesta:
        if e1 in sorteo:
            aciertos += 1
    return aciertos

# PROGRAMA QUE HACE ALGO
numeros_sorteo = sortear()

apuesta_usuario = pedir_numeros(6)

aciertos = comparar_listas(apuesta_usuario, numeros_sorteo)

if aciertos < 3 :
    print('Perdiste')
    print('Los números sorteados son:', numeros_sorteo)
elif aciertos >= 3 and aciertos < 6:
    print('Ganaste un premio de consuelo por', aciertos,'aciertos')
    print('Los números sorteados son:', numeros_sorteo)
else:
    print('Ganaste!!!!')
    print('Los números sorteados son:', numeros_sorteo)












    

