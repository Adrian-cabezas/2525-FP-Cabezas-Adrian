# Paso 1: Tenemos que crear la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Tenemos que Calcula el monto del descuento aplicando un porcentaje cualquiera a nuestro monto total de la compra.

    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Paso 2: Tenemos que llamar a la función desde el programa principal

# Primera llamado : Solo se proporciona el monto total
monto_compra_1 = 500.00
descuento_1 = calcular_descuento(monto_compra_1)
print(f"Primera Compra : Monto total= ${monto_compra_1}")
print(f"Tu descuento aplicado es 10% = ${descuento_1:.2f}")
print(f"Monto final a pagar = ${monto_compra_1 - descuento_1:.2f}\n")

# Segunda llamado : Proporcionar el monto total y un porcentaje de descuento
monto_compra_2 = 1200.00
porcentaje = 25
descuento_2 = calcular_descuento(monto_compra_2, porcentaje)
print(f"Segunda Compra : Monto total = ${monto_compra_2}")
print(f"Tu descuento aplicado es ({porcentaje}%) = ${descuento_2:.2f}")
print(f"Monto final a pagar = ${monto_compra_2 - descuento_2:.2f}")
