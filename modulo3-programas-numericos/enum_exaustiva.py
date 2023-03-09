objetivo = int(input('Introduce un numero: '))

respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')
else:
    print(f'El {objetivo} no tiene una raiz cuadrada exacta')
