"""
Un tupla es parecido a un array, sin embargo tienen algunas diferencias.
Las tuplas no pueden cambiar su valor, los arrays si. 
De resto son practicamente iguales, salvo que un array se define como [] y una tupla ()
"""

my_tuple = (1, 'dos', True)
# esto devuelve un int, ya que para ser tupla tiene que tener una, despues del primer elemento
no_es_tupla = (1)

my_other_tuple = (4,)

my_tuple += my_other_tuple


def coordenadas(): return (5, 4)


# Ahora coordenada contiene la tupla que devuelve la funcion coordenadas()
coordenada = coordenadas()

print(coordenada)

x, y = coordenadas()

print(x, y)
