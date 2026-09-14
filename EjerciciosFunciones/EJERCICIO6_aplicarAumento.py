def aplicar_aumento(precio):
    precio = precio + 100
    print("Precio dentro:", precio) # La variable precio es local en la funcion y por ende no afecta a la variable global precio_producto


precio_producto = 500
aplicar_aumento(precio_producto)

print("Precio fuera:", precio_producto)