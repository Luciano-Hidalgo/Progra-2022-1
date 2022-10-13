# EJERCICIO 1:
# MAGIA NEGRA QUE PIDE UNA LISTA, Y LA TRANSFORMA AUTOMÁTICAMENTE A UNA LISTA DE ENTEROS
print('Ejercicio 1:')
lista = list(map(int,input('Ingrese una lista de números enteros, separados por espacio:').split(' ')))

valor = int(input('Ingrese el valor a evaluar: '))

i = 0
esta = -1
while i < len(lista):
    if valor == lista[i]:
        esta = i
        i = len(lista)
    i = i + 1

if esta != -1:
    print('El número', valor,'está en la posición', esta)
else:
    print('El número', valor, 'no se encuentra en la lista')

# EJERCICIO 2
print('\nEjercicio 2:')
lista = list(map(int,input('Ingrese una lista de números enteros, separados por espacio:').split(' ')))

valor = int(input('Ingrese el valor a evaluar: '))

i = 0
contador = 0
while i < len(lista):
    if valor == lista[i]:
        contador = contador + 1
    i = i + 1

print('El elemento', valor,'se encuentra', contador, 'veces en la lista')


# EJERCICIO 3
print('\nEjercicio 3:')
lista = list(map(int,input('Ingrese una lista de números enteros, separados por espacio:').split(' ')))

i = 1
ordenada = True
while i < len(lista):
    if lista[i - 1] > lista[i]:
        ordenada = False
    i = i + 1

if ordenada:
    print('La lista está ordenada')
else:
    print('La lista no está ordenada')
    
