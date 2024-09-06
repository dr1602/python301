import random

def ordenamiento_mezcla(lista):
    # ordenamiento recursivo, mezclar como ejecutamos una y otra vez la misma funcion
    # y luego haremos iteraciones como en buble y busqueda binaria dentro de la recursion
    # tiene un crecimiento logaritmico
    if len(lista) > 1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # print(izquierda, '*' * 5, derecha)
        
        # llamada recursiva en cada mitad, hasta que no se puedan dividir mas
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)
        
        # Iteradores para recorrer sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0
        
        # se comparan primero mientras si pueden comparar
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1
            
        # si queda algo a la izuierda, se pega
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
            
        # si quedo algo de la derecha, se pega
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            
        # pintar comparaciones y como se van construyendo
        # print(f'izquierda {izquierda}, derecha {derecha}')
        # print(lista)
        # print('-' * 21)
    
    return lista
            

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista?: '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(f'Esta es la lista desorden: {lista}')
    print('-' * 21) # divisor con una linea por 21 veces
    
    lista_ordenada = ordenamiento_mezcla(lista)
    print(f'Esta es la lista ordenada: {lista_ordenada}')