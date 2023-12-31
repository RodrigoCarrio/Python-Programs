'''
Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
alumnos = [[],[],[]]
materias = []

import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
1. Ver lista de alumnos
2. Permitir al usuario del programa agregar un nuevo alumno
3. Editar la edad de un alumno por el nombre.
4. Ver lista de materias
5. Agregar materias al sistema
6. Salir.
Opcion: """)
    if opcion == "1":
        fu.view_students(alumnos)  
    elif opcion == "2":
        fu.add_student(alumnos)
    elif opcion == "3":
        fu.change_age_student(alumnos)
    elif opcion == "4":
        fu.view_subjects(materias)
    elif opcion == "5":
        fu.add_subjects(materias)
    elif opcion == "6":
        break
    else:
        print("No ingresó una opcion.")