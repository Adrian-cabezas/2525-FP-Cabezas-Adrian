# Titulo "Diccionario Inicial"
informacion_personal_inicial = {
    "nombre": "Ana López",
    "edad": 21,
    "ciudad": "Quito",
    "profesion": "Diseñadora Gráfica"
}

print("--- Diccionario Inicial con Datos Separados ---")
# Imprimimos los datos del diccionario inicial separados
for clave, valor in informacion_personal_inicial.items():
    print(f"{clave.capitalize()}: {valor}")
print("-" * 30) # Separador visual

# Tenemos que hacer una copia para ir modificando y no alterar el original
informacion_personal_final = informacion_personal_inicial.copy()

# Acceder y Modificar Valores
informacion_personal_final["ciudad"] = "Guayaquil"
informacion_personal_final["profesion"] = "Ilustradora digatal"

# Ver las existencia de Claves y Agregar los valores requeridos
if "telefono" not in informacion_personal_final:
    informacion_personal_final["telefono"] = "0920227289"

# Eliminar la Clave elegida
if "edad" in informacion_personal_final:
    del informacion_personal_final["edad"]

print("--- Operaciones Realizadas ---")
print("Ciudad modificada a: Guayaquil")
print("Profesión actualizada a: Ilustradora digital")
print("Teléfono agregado: 0920227289")
print("Edad eliminada.")
print("-" * 21) # Hacer la separación visual

# Por ultimo imprimir el diccionario Final, dato a dato
print("--- Diccionario Final con los Datos Separados ---")
for clave, valor in informacion_personal_final.items():
    print(f"{clave.capitalize()}: {valor}")