"""
El programa debe:
* contar con 4 funciones:
    1. Conversor de Grados Celcius a Fahrenheit.
    2. Conversor de cm3 a litros
    3. Conversor de litros a cm3.
    4. Pesos a USD
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 parametros y devolver el resultado al usuario    
* gestionar posibles errores
"""

import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
    1. Conversor de Grados Celcius a Fahrenheit.
    2. Conversor de cm3 a litros
    3. Conversor de litros a cm3.
    4. Pesos a USD
    5- Salir
Opcion: """)
    if opcion == "1":
        print(fu.celcius_a_fahrenheit(50))        
    elif opcion == "2":
        print(fu.cm3_a_litros(2580))
    elif opcion == "3":
        print(fu.litros_a_cm3(4))
    elif opcion == "4":
        print(fu.pesos_a_usd(14000))
    elif opcion == "5":
        break
    else:
        print("No ingresó una opcion.")