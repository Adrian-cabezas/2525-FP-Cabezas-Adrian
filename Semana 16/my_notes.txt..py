# 1 Crear un archivo de texto llamado my_notes.txt
archivo_para_escribir = open("my_notes.txt", "w")

# Debemos escribir la primera nota personal
archivo_para_escribir.write("Nota numero uno : El dia de hoy estuve aprendiendo a crear archivos en Python.\n")

# Debemos escribir la segunda nota personal
archivo_para_escribir.write("Nota numero dos : Me resulta muy interesante saber este tipo de lenguaje de programacón.\n")

# Debemos escribir la tercera nota personal
archivo_para_escribir.write("Nota numero tres: Tengo que practicar para asi mejorar mi programación.\n")

# Luego tenemos que cerrar el archivo después de escribir
archivo_para_escribir.close()

# 2 Abrir el archivo para leerlo
archivo_para_leer = open("my_notes.txt", "r")

# Poder leer la primera línea y mostrarla en la consola
linea1 = archivo_para_leer.readline()
print(linea1)

# Con la segunda línea mostrarla en la consola
linea2 = archivo_para_leer.readline()
print(linea2)

# Y con la tercera línea poder mostrarla en la consola
linea3 = archivo_para_leer.readline()
print(linea3)

# Luego debemos cerrar el archivo después de leer
archivo_para_leer.close()

# El fin del programa
print(" Este archivo fue leído y cerrado correctamente.")