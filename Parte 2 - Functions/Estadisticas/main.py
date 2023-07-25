"""
Crear un programa que debe:
* Simular un programa que calcule estadisticas
* Pedir al usuario una serie de numertos enteros del 1 al 10 y guardarlos en una lista hasta que el usuario ingrese "fin".
* Mostrar un menu con 4 opciones
    1. Calcular promedio
    2. Verificar cuantos numeros son menores que el numero indicado por el usuario
    3. Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
    4. Verifica si un numero que desee el usuario está en la lista.
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
import Functions as fu

fu.pedir_numeros()
while True:
    opcion = input("""
Ingrese una opcion:
    1. Calcular promedio
    2. Verificar cuantos numeros son menores que el numero indicado por el usuario
    3. Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
    4. Verifica si un numero que desee el usuario está en la lista.
    5. Salir
Opcion: """)

    if opcion == "1":
        fu.calcular_promedio()                
    elif opcion == "2":
        fu.verificar_numeros_menores()        
    elif opcion == "3":
        fu.verificar_numeros_mayores()        
    elif opcion == "4":
        fu.verificar_numero()
    elif opcion == "5":
        break        
    else:
        print("No ingresó una opcion.")