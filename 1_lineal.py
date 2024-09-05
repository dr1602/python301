import random

def busqueda_lineal(lista, objetivo):
    match = False
    i = 0
    for elemento in lista: #O(n)  
        i += 1
        print(f'Las veces que se ha ejecutado el codigo son: {i}')
        if elemento == objetivo:
            match = True
            break
            # no modifica la complejidad algoritmica pero en promedio nos tardariamos menos.
            # pero siempre hay que pensar en el peor escenario o no existe?
            # el brake no servira de nada.
            
    return match

# generar pequenio programar para generar listas, y preguntar cual seria el objetivo

if __name__ == '__main__':
    # para importar y que se pueda ejecutar directamente el codigo
    tamano_de_lista = int(input('De que tamano sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    
# cual es su complejidad algoritmica.
# La funcion crece en O(n), O de N. O lineal