my_range = range(1, 5)
type(my_range)

for i in my_range:
    print(i)


# Con esto el decimos que vaya desde el 0 al 7 (no inclusive) de 2 en 2

my_range = range(0, 7, 2)

my_other_range = range(0, 8, 2)

print(f'{my_range==my_other_range}')

for i in my_range:
    print(i)

for i in my_other_range:
    print(i)

# Esto ya nos devolveria false debido a que no son el mismo objeto
print(my_range is my_other_range)

for i in range(0, 101, 2):
    print(i)
