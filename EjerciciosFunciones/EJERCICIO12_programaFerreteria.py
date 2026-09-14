def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.08
    return 0


def calcular_iva(monto):
    return monto * 0.15

def mostrar_resumen(producto, subtotal, descuento, iva, total):
    print("--- RESUMEN DE VENTA ---")
    print("Producto:", producto)
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento: C$", round(descuento, 2))
    print("IVA: C$", round(iva, 2))
    print("Total: C$", round(total, 2))


producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: C$ "))
cantidad = int(input("Cantidad: "))

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal)

monto_con_descuento = subtotal - descuento

iva = calcular_iva(monto_con_descuento)
total = monto_con_descuento + iva

mostrar_resumen(producto, subtotal, descuento, iva, total)


## En Python, los parámetros como precio, cantidad, subtotal y monto reciben dentro de la función una referencia al valor que se está utilizando. 
# Cuando son tipos inmutables como int, float o str, si modificamos el parámetro dentro de la función, la variable original no cambia.