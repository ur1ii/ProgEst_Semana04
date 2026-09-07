import aritmetica as ar

def menu():
    print("=== Bienvenidos a mi calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

    op = int(input("Ingresa el # de la opcion deseada: "))
    return op


def showAdd(num1, num2):
    print(f"La suma de {num1} + {num2} es: {ar.add(num1, num2)}")


def showSub(num1, num2):
    print(f"La resta de {num1} - {num2} es: {ar.sub(num1, num2)}")


def showMult(num1, num2):
    print(f"La multiplicacion de {num1} * {num2} es: {ar.mult(num1, num2)}")


def showDiv(num1, num2):
    print(f"La division de {num1} / {num2} es: {ar.div(num1, num2)}")


def readValues():
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    return num1, num2


def choose(op):
    if op == 1:
        num1, num2 = readValues()
        showAdd(num1, num2)
    elif op == 2:
        num1, num2 = readValues()
        showSub(num1, num2)
    elif op == 3:
        num1, num2 = readValues()
        showMult(num1, num2)
    elif op == 4:
        num1, num2 = readValues()
        showDiv(num1, num2)
    elif op == 0:
        print("Adios")

def main():
    while True:
        op = menu()
        if op == 0: break
        if op > 0 and op <=4: choose(op)
        else: print("Opcion invalida...")

main()
