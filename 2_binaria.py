import random

def busqueda_binaria(lista, inicio, final, objetivo):
    # haremos un print statement para saber que sucede dentro
    print(f'buscando {objetivo} entre {lista[inicio]} y {lista[final-1]}')
    if inicio > final:
        return False

    medio = (inicio + final) // 2
    
    # si el valor buscado es igual que la mitad
    if lista[medio] == objetivo:
        return True
    # si el valor buscado es mayor que la mitad
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    # si el valor buscado es menor que la mitad
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))
    
    # como asume que la info esta ordenada, la ordenamos aqui
    
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    
    # usaremos indices para recorrer la lista, en lugar de solo hacer listas mas pequenias
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    
# para recursivadad, recuerda que luego de cada ejecucion se genera un nuevo frame y los valores van cambiando.
