#Búsqueda en Arreglo Multidimensional
def buscar_en_matriz(matriz, valor_buscado):
    """Busca un valor en una matriz bidimensional y devuelve su posición."""
    for i, fila in enumerate(matriz):
        try:
            j = fila.index(valor_buscado)
            return (i, j)
        except ValueError:
            continue
    return None


mi_matriz = [
    [1, 5, 9],
    [3, 7, 2],
    [8, 4, 6]
]

while True:
    try:
        valor_a_encontrar = int(input(" Ingresa el número a buscar en la matriz : "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

# Buscar y mostrar resultado
posicion = buscar_en_matriz(mi_matriz, valor_a_encontrar)

if posicion:
    print(f"\nFelicidades el valor {valor_a_encontrar} está en la fila {posicion[0]}, columna {posicion[1]}.")
else:
    print(f"\nEl valor {valor_a_encontrar} no se encuentro en la matriz.")

print("\nMatriz:")
for fila in mi_matriz:
    print(fila)