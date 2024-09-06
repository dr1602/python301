def morral(tamano_morral, pesos, valores, n):
    # Caso base: no hay más elementos o el morral está lleno
    if n == 0 or tamano_morral == 0:
        print(f'[Caso Base] No hay más elementos o morral lleno.')
        print(f'Tamaño morral restante: {tamano_morral}, Elementos restantes: {n}')
        return 0

    # Si el peso del elemento actual es mayor al tamaño restante del morral
    if pesos[n - 1] > tamano_morral:
        print(f'[Excluyendo] Peso del elemento {n} ({pesos[n - 1]}) es mayor que el tamaño del morral ({tamano_morral}).')
        # Se excluye el elemento n
        return morral(tamano_morral, pesos, valores, n - 1)

    # Decisión de incluir o no incluir el elemento n
    print(f'[Decisión] Evaluando elemento {n}:')
    print(f'  Peso: {pesos[n - 1]}, Valor: {valores[n - 1]}, Tamaño morral restante: {tamano_morral}')

    # Calcular el valor máximo entre incluir o no incluir el elemento n
    incluir = valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    excluir = morral(tamano_morral, pesos, valores, n - 1)
    
    print(f'  [Resultados] Incluir elemento {n} ({valores[n - 1]}): {incluir}, Excluir: {excluir}')
    
    return max(incluir, excluir)


if __name__ == '__main__':
    tamano_morral = 50
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    n = len(valores)
    
    resultado = morral(tamano_morral, pesos, valores, n)
    print(f'Resultado final: {resultado}')
