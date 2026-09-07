"""
Operaciones basicas:
suma, resta, multiplicacion y division
"""

def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1 * number2

def div(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "No se pueded dividir entre 0"
    except TypeError:
        return "Tipo de dato incorrecto, debe ingresar un numero"