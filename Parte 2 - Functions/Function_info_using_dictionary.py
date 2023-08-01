"""
Crear una funcion que debe: (usar diccionario)

    * Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario.
    * Mostrar por pantalla el mensaje: "nombre" tiene "edad" años, vive en "direccion" y su número de teléfono es "telefono".
"""
datos = {}

def ask_information():
    while True:
        name = input("Ingrese su nombre: ").casefold().capitalize()
        address = input("Ingrese la direccion: ")
        try:
            age = int(input("Ingrese su edad: "))
            phone = int(input("Ingrese numero de telefono "))
            if age > 0:
                datos.update({"Name" : name})
                datos.update({"Address" : address})
                datos.update({"Age" : age})
                datos.update({"Phone" : phone})
                print(datos)
                print(f"{name} tiene {age} años, vive en {address} y su numero de telefono es {phone}")
                break
            else:
                print("La edad debe ser mayor a 0")
        except:
            print("Error al ingresar edad y/o telefono.")
        

ask_information()