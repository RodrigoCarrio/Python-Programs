"""
El programa debe:
* contar con 4 funciones: suma, resta, multiplicacion y division
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 numeros para operar y devolver el resultado al usuario    
* no deben generar errores
"""
import Functions as fu
while True:
    opcion = input("""
Ingrese una opcion:
1- Suma
2- Resta
3- Multiplicacion
4- Division
5- Salir
Opcion: """)
    if opcion == "1":
        a,b = fu.pedir_numeros()
        print(f"La suma de {a} + {b} es= {fu.suma(a,b)} ")
    elif opcion == "2":
        a,b = fu.pedir_numeros()
        print(f"La resta de {a} - {b} es= {fu.resta(a,b)} ")
    elif opcion == "3":
        a,b = fu.pedir_numeros()
        print(f"La multiplicacion de {a} * {b} es= {fu.multiplicacion(a,b)} ")
    elif opcion == "4":
        a,b = fu.pedir_numeros()
        print(f"La division de {a} / {b} es= {fu.division(a,b)} ")
    elif opcion == "5":
        break
    else:
        print("No ingresó una opcion.")