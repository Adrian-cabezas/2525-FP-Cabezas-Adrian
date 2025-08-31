#Ordenación de Arreglo Multidimensional
def bubble_sort(fila):
    """
    Ordena una lista usando el algoritmo Bubble Sort en orden ascendente.
    """
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


def ordenar_fila(matriz, fila_index):
    """
    Ordena una fila específica de la matriz utilizando Bubble Sort.
    """
    if 0 <= fila_index < len(matriz):
        matriz[fila_index] = bubble_sort(matriz[fila_index])
    else:
        print("️ Índice de fila fuera de rango.")
    return matriz


def mostrar_matriz(matriz):
    """
    Imprime la matriz en formato de tabla.
    """
    for fila in matriz:
        print(fila)
    print()


if __name__ == "__main__":
    matriz = [
        [9, 2, 7],
        [4, 6, 1],
        [5, 3, 8]
    ]

    print(" Matriz original:")
    mostrar_matriz(matriz)


    try:
        fila_a_ordenar = int(input(f" Ingresa el número de fila a ordenar (0,1,2):"))
        matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

        print(f"\n Matriz con la fila {fila_a_ordenar} ordenada:")
        mostrar_matriz(matriz_ordenada)

    except ValueError:
        print("️ Debes ingresar un número entero válido.")