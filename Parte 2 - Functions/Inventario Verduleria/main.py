"""
Crear un programa que debe:
* Contar con un stock de frutas y otro de verduras (el stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias.
* Contar con 3 funciones
    1. Agregar frutas o verduras al correspondiente stock
    2. Consultar el stock
    3. Eliminar un elemento del stock
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
    1. Agregar frutas o verduras al correspondiente stock
    2. Consultar el stock
    3. Eliminar un elemento del stock
    4- Salir
Opcion: """)
    if opcion == "1":
        fu.add_frutas_verduras()       
    elif opcion == "2":
        fu.consultar_stock()
    elif opcion == "3":
        fu.delete_frutas_verduras()
    elif opcion == "4":
        break
    else:
        print("No ingresó una opcion.")