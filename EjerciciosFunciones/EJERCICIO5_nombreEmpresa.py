#1. Crea una variable global llamada nombre_empresa y muéstrala dentro de una función.
#2. Crea una función con una variable local llamada total. Intenta utilizarla fuera de la función, observa el error y explícalo.
#3. Crea un contador global y modifícalo desde una función mediante global.

global nombre_empresa

def showName():
    global nombre_empresa
    nombre_empresa = "HUMBERTO Y ASOCIADOS"
    print(nombre_empresa)
    
showName()

def calculateTotal():
    total = 100
    print(total)

calculateTotal()
# print(total), El error proviene de que la variable es local, para arreglarlo, se podría declarar como variable global

counter = 0
def addCounter():
    global counter
    counter += 1

print(counter) 
addCounter()   
print(counter)