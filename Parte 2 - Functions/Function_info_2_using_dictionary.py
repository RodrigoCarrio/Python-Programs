"""
Crear una funcion que debe: (usar diccionario)

    * Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
    * Pida al usuario el dato a agregar (key) y el valor
    * Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
information = {}

def add_info_person(dictionary):
    while True:
        try:
            key = input("Ingrese el atributo de la persona(Ej: Nombre, etc) o ingrese exit para salir: ").casefold().capitalize()
            if key == "Exit":
                break
            value = input(f"Ingrese el valor del atributo '{key}': ")
            dictionary.update({key : value})
            print(dictionary)
        except:
            print("Error")

add_info_person(information)