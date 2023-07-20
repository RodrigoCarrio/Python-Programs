"""
El programa debe: 
* pedir al usuario que ingrese la cantidad de dinero que dispone.
* verificar que la cantidad ingresada es un numero y sino mostrar un error.
* verificar la cantidad ingresada e indicar que auto o autos puede comprar.
"""

ford = 10000
renault = 11000
chevrolet = 15000

while True:
    try:
        dinero_usuario = int(input("Ingrese la cantidad de dinero que dispone: "))
        if (dinero_usuario >= chevrolet):
            print(f"La cantidad ingresada es de ${dinero_usuario} y puede comprar cualquier marca.")
        elif dinero_usuario < ford:
            print(f"La cantidad ingresada es de ${dinero_usuario} y no puede comprar algun auto.")
        else:
            print(f"La cantidad ingresada es de ${dinero_usuario} y puede comprar Ford o Renault.")
    except:
        print("Error. No ingreso valores numericos enteros.")
