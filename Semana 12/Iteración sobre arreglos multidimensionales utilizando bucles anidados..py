# Tarea: Iteración sobre arreglos multidimensionales utilizando bucles anidados.
# Temperaturas Diarias / ciudad / semanas / dias.
ciudades = ["Guayaquil" , "Esmeraldas" , "Ambato"]
semana = 2
dias = [ "Lunes" ,"Martes" , ",Miercoles" , " Jueves " , " Viernes" , "Sabado" , " Domingo "]

temperaturas = [
    [
       [28, 29, 35, 32, 29, 31, 33] ,   # Semana 1
       [27, 34, 31, 29, 30, 29, 32]     # Semana 2
    ] ,
    [
       [30, 32, 30, 34, 35, 31, 33] ,   # Semana 1
       [35, 29, 35, 32, 33, 36, 34]     # Semana 2
    ] ,
    [
       [11, 10, 13, 12, 15, 14, 19],    # Semana 1
       [14, 12, 13, 15, 14, 10, 13]     # Semana 2
    ]
]

for i, ciudad in enumerate(ciudades):
    print(f'\nCiudad: {ciudad}')
    for semana in range(2) :
        suma = 0
        for dia in range(7):
            suma += temperaturas[i][semana][dia]
        promedio = suma /7
        print(f'  Semana {semana + 1}: Promedio = {promedio:.2f}  ºC ')

