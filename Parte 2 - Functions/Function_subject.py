"""
Crear una funcion
* Pedir al usuario 5 materias (Ej: Matematicas, Fisica, Quimica, Historia, etc.)
* Verificar que sea un nombre correcto
* Almacenar los nombres en una lista 
* Mostrar las materias en orden alfabetico  
* gestionar posibles errores
"""

def subjects():
    lista = []
    i = 0
    while i<5:
        materias = input("Ingrese las materias que desea: ").capitalize()
        if materias.isalpha():
            lista.append(materias)
            i += 1
            print(f"La materia {materias} fue agregada con exito.")
        else:
            print("Ingrese palabras alfabeticas.")
    lista.sort()
    print(f"Las materias son: {lista} ")

subjects()


