class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


nombre1 = input("Introduce el nombre del primer usuario: ")
edad1 = int(input("Introduce la edad del primer usuario: "))
print(edad1)
user1 = Usuario(nombre1, edad1)
nombre = input("Introduce el nombre del primer usuario: ")
edad = int(input("Introduce la edad del primer usuario: "))
user2 = Usuario(nombre, edad)

if(user1.edad < user2.edad):
    print(f'{user1.nombre} es menor que {user2.nombre}')
elif(user1.edad > user2.edad):
    print(f'{user1.nombre} es mayor que {user2.nombre}')
else:
    print(f'{user1.nombre} y {user2.nombre} tienen la misma edad')
