
def calcular_pago(horas, tarifa):
    global pago
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)
    
calcular_pago(40, 120)
print(pago)

# La siguiente instrucción produciría NameError:
# print(pago)