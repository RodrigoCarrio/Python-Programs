"""
Crear un programa que debe:
* Contar con un stock de frutas y otro de verduras (el stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias.
* Contar con 3 funciones
    1. Agregar frutas o verduras al correspondiente stock
    2. Consultar el stock
    3. Eliminar un elemento del stock
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
frutas_stock = []
verduras_stock = []

def add_frutas_verduras():
    while True:
        stock = input("""
    Elija un stock para agregar fruta o verdura.
    1. Frutas
    2. Verduras
    3. Salir
opcion: """)
        if stock == "1":
            print("Stock de Frutas")
            fruta = input("Ingrese la fruta que desea: ").casefold()
            if (fruta.isalpha()) and (fruta not in frutas_stock) :
                frutas_stock.append(fruta)
                print(f"Se agregó la fruta {fruta} al stock.")
            else: 
                print("No ingresó una palabra o la fruta ya se encuentra en el stock.")

        elif stock == "2":
            print("Stock de Verduras")
            verdura = input("Ingrese la verdura que desea: ").casefold()
            if (verdura.isalpha()) and (verdura not in verduras_stock) :
                verduras_stock.append(verdura)
                print(f"Se agregó la verdura {verdura} al stock.")
            else: 
                print("No ingresó una palabra o la fruta ya se encuentra en el stock.")
        
        elif stock == "3":
            break
        else:
            print("Opcion incorrecta.")

def consultar_stock():
    while True:
        opcion = input("""
    Seleccione el stock a consultar
    1. Frutas
    2. Verduras
    3. Salir
opcion: """)
        if opcion == "1":
            print("STOCK DE FRUTAS")
            for i in range(0,len(frutas_stock)):
                print(frutas_stock[i])

        elif opcion == "2":
            print("STOCK DE VERDURAS")
            for i in range(0,len(verduras_stock)):
                print(verduras_stock[i])

        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta.")

def delete_frutas_verduras():
    while True:
        stock = input("""
    Elija un stock para eliminar fruta o verdura.
    1. Frutas
    2. Verduras
    3. Salir
opcion: """)
        if stock == "1":
            print(frutas_stock)
            fruta = input("Ingrese la fruta a eliminar: ").casefold()
            if fruta in frutas_stock:
                frutas_stock.remove(fruta)
                print(f"Se eliminó la fruta {fruta} del stock.")
            else:
                print(f"No se encuentra la fruta {fruta} en el stock.")

        elif stock == "2":
            print(verduras_stock)
            verdura = input("Ingrese la verdura a eliminar: ").casefold()
            if verdura in verduras_stock:
                verduras_stock.remove(verdura)
                print(f"Se eliminó la verdura {verdura} del stock.")
            else:
                print(f"No se encuentra la verdura {verdura} en el stock.")

        elif stock == "3":
            break
        else: 
            print("Opcion incorrecta.")

        

