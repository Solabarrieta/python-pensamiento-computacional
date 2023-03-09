def enum_exahustiva(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1

    return respuesta


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    return respuesta


def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return respuesta


""" 
tambien podemos definir funciones en expresiones
con el keyword lambda 
lambda <variables>: <expresiones>

sumar = lambda x,y : x + y 
"""

""" 
tambien podemos guradar operaciones en estructuras de datos 
por ejemplo ...
"""


def aplicar_operaciones(num):
    """
    Esta funcion pasa a valor absoluto y a float culquier numero entero

    num int 
    return array con el valor absoluto de num y su conversion float
    """
    operaciones = [abs, float]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    return resultado


numero = int(input('Escribe un entero: '))

print(f'El resultado es {aplicar_operaciones(numero)}')
