numero = 100

for i in range(0,numero, 5):
    print(i)
'''
numero = int(input('Ingrese un número entero positivo:'))

es_primo = True
for i in range(2,numero):
    print(i)
    if numero % i == 0:
        es_primo = False

if es_primo:
    print('El número es primo')
else:
    print('El número no es primo')

'''
'''
numero = int(input('Ingrese un número entero positivo:'))

aux = 2
contador = 0
while contador < numero:
    es_primo = True
    i = 2
    while i < aux:
        if aux % i == 0:
            es_primo = False
            i = aux
        i = i + 1

    if es_primo:
        print(aux)
        contador = contador + 1
    
    aux = aux + 1
'''
