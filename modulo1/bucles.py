# WHILEs

while True:
    if True:
        print(
            "Este bucle se imprimira infinitas veces... Menos esta porque tiene un Break ;)")
        break

contador = 0

while contador < 10:
    print(contador)
    contador += 1

contador = 10

frutas = ['manzana', 'pera', 'mango']

for fruta in frutas:
    print(fruta)

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4
}

for pais in estudiantes:  # Devuelve el nombre del atributo
    print(pais)

for pais in estudiantes.keys():  # Lo mismo que el de arriba
    print(pais)

for num_estudiantes in estudiantes.values():  # Devuelve el valor de cada key
    print(num_estudiantes)

for pais, num_estudiantes in estudiantes.items():
    print(f'El pais {pais} y sus estudiantes {num_estudiantes}')


'''
Los siguientes for no se pueden hacer con enteros debido a que un entero no es un objeto que la funcion iter() pueda devolver un iterable
for n in contador:
    print(contador1)
'''
