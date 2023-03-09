import sys

print(sys.getrecursionlimit())


def comprobar(n):
    if n == 1:
        return 1
    print(n)
    return comprobar(n-1)


n = int(input('Introduce un entero: '))


print(comprobar(n))
