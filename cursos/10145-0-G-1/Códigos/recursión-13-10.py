def sumar_digitos(n):
    """Sumar los dígitos de un
    entero no negativo.
    Entrada: entero no negativo.
    Salida: entero no negativo."""
    if n < 10: 
        return n
    ultimo = n % 10                                                       
    n = n // 10 
    return ultimo + sumar_digitos(n) 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_it(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial = i * factorial
        i = i + 1
    return factorial


    
def validar(texto):
    '''Solicita un entero,
        si el entero ingresado es válido lo retorna
        sino, lo pide de nuevo
    '''
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
    return validar(texto)


def multiplicar_it(val_1, val_2):
    acum = 0
    i = 0
    while i < val_2:
        acum += val_1
        i += 1
    return acum

def multiplicar_rec(val_1, val_2):
    # Caso base
    # Si ya no tengo que sumar más veces
    if val_2 == 1:
        return val_1
    # Regla de recurrencia
    return val_1 + multiplicar_rec(val_1, val_2 - 1)


# DESCOMPOSICIÓN PRIMA
# 100 = 2 * 2 * 5 * 5
# 121 = 11 * 11
# 360 = 2 * 2 * 2 * 3 * 3 * 5
def es_primo(n):
    i = 2
    while i < n:
        if n% i == 0:
            return False
        i = i + 1
    return True

def descomposicion_prima_it(numero):
    i = 2
    lista = []
    while i <= numero:
        if numero % i == 0 :
            numero = numero // i
            lista.append(i)
        else:
            i = i + 1
    return lista

def descomposicion_prima_rec(numero, i=2):
    # CASO BASE
    # Si el número con el que estoy dividiendo
    # es igual al número que estoy buscando
    if i == numero:
        print(i)
        return None
    if numero % i == 0:
        print(i)
        numero = numero // i
        return descomposicion_prima_rec(numero, i)
    else:
        return descomposicion_prima_rec(numero, i + 1)

'''
def descomposicion_prima(numero):
    return descomposicion_prima_rec(numero, 2)
'''


    
    
