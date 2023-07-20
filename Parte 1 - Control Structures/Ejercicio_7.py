"""
El programa debe: 
* pedir el ingreso de un numero positivo al usuario y almacenar la respuesta en la variable "numero".
* verificar que se trate de un numero entero y sino mostrar un error.
* Comprobar si el numero es negativo. Si lo es, el programa deve avisar que no era eso lo que se habia pedido.
* imprimir el valor introducido por el usuario
"""

while True:
    try:
        numero = int(input("Ingrese un numero positivo: "))
        if numero >= 0:
            print(f"El valor ingresado por el usuario es: {numero}. ")
            break
        else:
            print("El numero ingresado no es positivo.")
    except:
        print("Error. No ingreso un numero entero.")