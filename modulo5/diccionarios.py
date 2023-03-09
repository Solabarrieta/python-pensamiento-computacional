my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}

print(my_dict['David'])

my_dict.get('Juan', 30)

my_dict['Jaime'] = 20

my_dict['Pedro'] = 70

del my_dict['Jaime']

for llave in my_dict.keys():
    print(llave)

for valor in my_dict.values():
    print(valor)

for llave, valor in my_dict.items():
    print(llave, valor)


print(f'{"David" in my_dict}')
