def procesar_venta(subtotal):
    global calcular_iva
    def calcular_iva():
        return subtotal * 0.15

    iva = calcular_iva()
    return subtotal + iva

total = procesar_venta(2000)
print("Total: C$", total)
print("Iva: ", calcular_iva())

# calcular_iva() no está disponible fuera de procesar_venta.