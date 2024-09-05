import time
# generaremos dos implementaciones de factorial
# implementacion recursiva

def factorial_recursivo(n):
    if n == 1:
        return 1
        
    return n * factorial_recursivo(n - 1)


# implementacion reiterativa

def factorial_reiterativo(n):
    respuesta = 1
    
    while n > 1:
        respuesta *= n
        n -= 1
        
    return respuesta

if __name__ == '__main__':
    n = 100
    
    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    lapsed_time = final - comienzo
    print(f'Recursivo: {lapsed_time:.10f}') # esto quita el formato de la notacion cientifica
    
    comienzo = time.time()
    factorial_reiterativo(n)
    final = time.time()
    lapsed_time = final - comienzo
    print(f'Reiterativo: {lapsed_time:.10f}') # esto quita el formato de la notacion cientifica