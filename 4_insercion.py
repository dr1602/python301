'''

    Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
    Al principio, la sublista ordenada contiene un solo elemento, por lo que por
    definición se encuentra ordenada.

    A continuación se evalua el primer elemento dentro la sublista desordenada para
    que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

    La inserción se realiza al mover todos los elementos mayores al elemento que
    se está evaluando un lugar a la derecha.

    Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
    tanto, la lista se encontrará ordenada.

'''

def insertion(list):
    base_index = 0
    current_index = 1
    reversed_current_index = 1
    n = len(list)
    
    while n > current_index:
        if list[current_index - 1] > list [current_index]:
            while reversed_current_index > base_index and list[reversed_current_index - 1] > list[reversed_current_index]:
                list[reversed_current_index - 1], list[reversed_current_index] = list[reversed_current_index], list[reversed_current_index - 1]
                reversed_current_index -= 1
            current_index += 1
            reversed_current_index = current_index
        else:
            current_index += 1
            reversed_current_index = current_index
    
    return list

## guide

def ordenamiento_por_insercion(lista):
    
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            
        lista[posicion_actual] = valor_actual
        

if __name__ == '__main__':
    numbers = [7, 3, 2, 9, 8]
    
    lista_ordenada = insertion(numbers)
    print(f'Esta es la lista ordenada: {lista_ordenada}')
