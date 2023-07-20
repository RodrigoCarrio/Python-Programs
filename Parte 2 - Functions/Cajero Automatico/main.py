"""
El programa debe:
* Simular cajero automatico y pedir usuario y contraseña (user, 1234). Caso verdadero mostrar menu y en caso falso seguir pidiendo.
* En caso de mal ingreso de usuario o contraseña 3 veces, el programa debe detenerse.
* contar con 4 funciones:
    1. Consultar el saldo (inicio de 50000)
    2. Ingresar dinero y actualizar saldo
    3. Retirar dinero y actualizar saldo
    4. Salir y volver al menu de usuario y contraseña  
* gestionar posibles errores
"""
import Functions as fu

while True:
    condicion = fu.log_in()
    while condicion:
        opcion = input("""
    Ingrese una opcion:
        1. Consultar el saldo
        2. Ingresar dinero y actualizar saldo
        3. Retirar dinero y actualizar saldo
        4. Salir y volver al menu de usuario y contraseña
    Opcion: """)
        if opcion == "1":
            fu.consultar_saldo()        
        elif opcion == "2":
            fu.ingresar_dinero()
        elif opcion == "3":
            fu.retirar_dinero()
        elif opcion == "4":
            condicion=False
        else:
            print("No ingresó una opcion.")