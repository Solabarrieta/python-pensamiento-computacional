def factorial(n):
    """Caulcula el factorial de n. 

    n int > 0 
    return n !
    """
    if n == 1:
        return 1

    # print(n)

    return n * factorial(n-1)


n = int(input('Escribe un entero: '))

print(factorial(n))
