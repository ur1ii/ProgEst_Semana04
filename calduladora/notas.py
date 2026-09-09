# Leer n cantidad de notas decir si es aprendizaje inicial, fundamental, sastisfactorio y avanzando, mostrar todas las notas

notes = []
categorias = []

def showNotes():
    return notes


def addNote(note):
    notes.append(note)
    return 0


def showSize():
    return len(notes)



def readNote():
    advancedKnowlegde = 0
    satisfactoryKnowlegde = 0
    fundamentalKnowlegde = 0
    starterKnowlegde = 0
    failed = 0
    while True:
        try:
            op = input("Quiere ingresa una nota(S-N): ")
            if op.upper() == "S":
                note = int(input("Ingrese la nota: "))
            elif op.upper() == "N":
                            break
            if note > 0 and note < 100:
                addNote(note)
                if note >= 90:
                    advancedKnowlegde += 1
                    categorias.append("Aprendizaje Avanzado")
                elif note >= 80 and note < 90:
                    satisfactoryKnowlegde += 1
                    categorias.append("Aprendizaje Satisfactorio")
                elif note >= 70 and note < 80:
                    fundamentalKnowlegde += 1
                    categorias.append("Aprendizaje Fundamental")
                elif note >= 60 and note < 70:
                    starterKnowlegde += 1
                    categorias.append("Aprendizaje Inicial")
                elif note < 60:
                    failed += 1
                    categorias.append("Reprobado")
        except ValueError:
            print("Ingrese una nota valida")
    print("=== RESULTADO DE NOTAS ===")
    print(f"Avanzado: {advancedKnowlegde}")
    print(f"Satisfactorio: {satisfactoryKnowlegde}")
    print(f"Fundamental: {fundamentalKnowlegde}")
    print(f"Inicial: {starterKnowlegde}")
    print(f"Reprobado: {failed}")
    
