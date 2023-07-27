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
def view_students(matriz):
    print("-------------- INFORMACION DE ALUMNOS -------------")
    print("USUARIOS   -   EDAD  -     EMAIL")
    for i in range(len(matriz[0])):
        print(f"{matriz[0][i]}   -    {matriz[1][i]}    -    {matriz[2][i]}")

def add_student(matriz):
    while True:
        user = str(input("Ingrese nombre de usuario del alumno: "))
        email = str(input("Ingrese el email del alumno: "))
        try:
            age = int(input("Ingrese la edad: "))
            if (user not in matriz[0]) and (age >= 10 and age <= 18) and ("@"  in email):
                matriz[0].append(user)
                matriz[1].append(age)
                matriz[2].append(email)
                print(f"Se añadió con exito el alumno: {user} - {age} - {email} ")
                break
            else:
                print("Alumno ya registrado y/o error al cargar un dato.")
        except:
            print("Error en el ingreso de la edad.")

def change_age_student(matriz):
    while True:
        user = input("Ingrese el usuario del alumno: ")
        try:
            index = matriz[0].index(user)
            new_age = int(input("Ingrese nueva edad: "))
            if new_age >= 10 and new_age <= 18:
                matriz[1][index] = new_age
                print("Se cambió la edad con exito")
                break
            else:
                print("La edad debe estar entre 10 y 18 años.")
        except:
            print("No se encuentra el alumno.")

def view_subjects(array):
    print("-------------- INFORMACION DE MATERIAS -------------")
    for i in array:
        print(i)
        

def add_subjects(array):
    while True:
        subject = input("Ingrese la materia: ")
        if subject not in array:
            array.append(subject)
            break
        else:
            print(f"Ya se encuentra la materia {subject}")
