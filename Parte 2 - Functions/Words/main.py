"""
El programa debe:
* contar con 3 funciones:
    1. Contador de letras (letra,palabra): debe contar la cantidad de veces que aparece la letra pasada por argumento de una palabra o frase (ambos parametros)
    2. Comparador de palabra (palabra1 vs palabra2): debe comparar que palabra tiene mas letras. IMPORTANTE: debe ser palabras y no frases
    3. Quitador de vocales (palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales.
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 parametros y devolver el resultado al usuario    
* gestionar posibles errores
"""
import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
1- Contador de letras
2- Comparador de 2 palabras
3- Quitador de vocales
4- Salir
Opcion: """)
    if opcion == "1":
        fu.contador_letras("a","hola como andas")
    elif opcion == "2":
        fu.comparador_palabras()
    elif opcion == "3":
        fu.quitador_vocales()
    elif opcion == "4":
        break
    else:
        print("No ingresó una opcion.")