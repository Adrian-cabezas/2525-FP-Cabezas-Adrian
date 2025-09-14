def calcular_temperatura_promedio(ciudades, temperaturas, dias=None):
    """
    Calcula la temperatura promedio por ciudad y por semana.

    Parámetros:
        ciudades (list): Lista de nombres de ciudades.
        temperaturas (list): Lista 3D con temperaturas [ciudad][semana][dia].
        dias (list, opcional): Lista de nombres de días de la semana. Si no se provee, se asume 7 días.

    Retorna:
        dict: Diccionario con las ciudades como claves y listas de promedios por semana.
    """
    if not ciudades or not temperaturas:
        raise ValueError("Las ciudades y las temperaturas no pueden estar vacías.")

    # Definir los días por defecto si no se proporcionan
    if dias is None:
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Validar que el número de las ciudades coincidan con el número de elementos en temperaturas
    if len(ciudades) != len(temperaturas):
        raise ValueError(
            f"El número de ciudades ({len(ciudades)}) no coincide con el número de conjuntos de temperaturas ({len(temperaturas)}).")

    resultados = {}

    for i, ciudad in enumerate(ciudades):
        print(f'\nCiudad: {ciudad}')
        resultados[ciudad] = []

        # Ver que las ciudades tengan al menos una semana
        if len(temperaturas[i]) == 0:
            print("  No hay datos de temperaturas para esta ciudad.")
            continue

        for semana_idx, semana_temps in enumerate(temperaturas[i]):
            # Validar que haya datos de días
            if len(semana_temps) == 0:
                print(f"  Semana {semana_idx + 1}: Sin datos de días.")
                promedio = 0.0
            else:
                suma = sum(semana_temps)
                cantidad_dias = len(semana_temps)
                promedio = suma / cantidad_dias

            resultados[ciudad].append(promedio)
            print(f'  Semana {semana_idx + 1}: Promedio = {promedio:.2f} °C')

    return resultados


# Los Datos de ciudades
ciudades = ["Guayaquil", "Esmeraldas", "Ambato"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado",
        "Domingo"]  # Corregido: eliminé espacios y error tipográfico

temperaturas = [
    [
        [28, 29, 35, 32, 29, 31, 33],  # Semana 1 - Guayaquil
        [27, 34, 31, 29, 30, 29, 32]  # Semana 2 - Guayaquil
    ],
    [
        [30, 32, 30, 34, 35, 31, 33],  # Semana 1 - Esmeraldas
        [35, 29, 35, 32, 33, 36, 34]  # Semana 2 - Esmeraldas
    ],
    [
        [11, 10, 13, 12, 15, 14, 19],  # Semana 1 - Ambato
        [14, 12, 13, 15, 14, 10, 13]  # Semana 2 - Ambato
    ]
]

# La función
print("=== PROMEDIO DE TEMPERATURAS POR CIUDAD Y SEMANA ===")
resultados = calcular_temperatura_promedio(ciudades, temperaturas, dias)

# Esto es opcional para mostrar resultados estructurados
print("\n=== RESULTADOS ESTRUCTURADOS ===")
for ciudad, promedios in resultados.items():
    print(f"{ciudad}: {promedios}")