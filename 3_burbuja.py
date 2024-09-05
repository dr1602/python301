import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    
    # obtenemos la longitud de la lista para iterar en ella
    # recorremos la lista n veces
    for i in range(n):
        # recorremos la lista n veces otra vez
        for j in range(0, n - i - 1):
            # comparamos elementos adjacentes, si el primero es mayor, lo intercambiamos
            if lista[j] > lista[j + 1]:
                # destructuracion de lista en las posiciones j y j + 1 para ordenarlos inversamente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista?: '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    
    lista_ordenada = ordenamiento_burbuja(lista)
    print(f'Esta es la lista ordenada: {lista_ordenada}')
    
'''

El patron para saber que complejidad tiene son los dos for y uno anidado en el otro
es O(n^2)

'''