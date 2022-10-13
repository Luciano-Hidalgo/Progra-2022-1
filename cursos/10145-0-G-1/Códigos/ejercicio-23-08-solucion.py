# ENTRADA
x1 = input('Ingrese x1: ')
y1 = input('Ingrese y1: ')
x2 = input('Ingrese x2: ')
y2 = input('Ingrese y2: ')
# PROCESAMIENTO
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
aux_1 = x1 - x2
aux_2 = y1 - y2
aux_3 = aux_1 ** 2
aux_4 = aux_2 ** 2
resultado = (aux_3 + aux_4)** (1/2)
# SALIDA
print('La distancia entre:')
print('\tx1:', x1, ', y1:', y1)
print('\tx2:', x2, ', y2:', y2)
print('es:', resultado)
