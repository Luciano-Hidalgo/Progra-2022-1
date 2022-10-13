# Ingreso un valor
numero = input('Ingrese un valor: ')
# Cambio el tipo de dato de string a float
#numero = float(numero)
numero = int(numero)

# Si el número es cero
if numero == 0:
    print('El número es cero')
# Si el número positivo
elif numero > 0:
    print('El número es positivo')
# Si el número es negativo
else:
    print('El número es negativo')
   
'''
# Si el número es cero
if numero == 0:
    print('El número es cero')
# Si el número positivo
if numero > 0:
    print('El número es positivo')
# Si el número es negativo
if numero < 0:
    print('El número es negativo')
    
'''
