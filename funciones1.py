#Leer la edad de una persona y decir si es menor o mayor de edad
age = 0
def readAge():
    print("Dime tu edad")
    global age
    age = int(input())

def evalAge(age):
    return age >= 18

def show():
    print("Mayor de edad" if evalAge(age) else "Menor de de edad")

readAge()
show()