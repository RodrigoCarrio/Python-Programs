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
dinero_disponible = 50000 #global variable

#function log in
def log_in():
    flag = 0
    while (flag < 3):
        print("""
    -------- CAJERO AUTOMATICO --------
    """)
        usuario = input("USUARIO: ")
        contraseña = input("CONTRASEÑA: ")
        if (usuario == "user") and (contraseña == "1234"):
            flag = 0 
            return True
        else:
            print("Error en el usuario y/o contraseña")
            flag += 1
    print(f"Se le dió 3 intentos y los ingreso incorrectamente")
    return exit()
    
#function consult balance
def consultar_saldo():
    global dinero_disponible
    print(f"Su cuenta tiene un saldo de: ${dinero_disponible}")    
    return dinero_disponible

#function deposit cash
def ingresar_dinero():
    global dinero_disponible
    while True:
        try:
            monto = int(input("Ingrese cantidad de dinero a depositar: "))
            if monto <= 0:
                print("Ingrese montos superiores a 0")
            else:
                dinero_disponible += monto
                return dinero_disponible
        except:
            print("Error.")

#function withdraw cash     
def retirar_dinero():
    global dinero_disponible
    while True:
        try:
            monto = int(input("Ingrese cantidad de dinero a retirar: "))
            if monto <= 0:
                print("Ingrese montos superiores a 0")
            elif monto > dinero_disponible:
                print("No puede ingresar un monto superior al saldo de la cuenta.")
            else:
                dinero_disponible -= monto
                return dinero_disponible
        except:
            print("Error.")
