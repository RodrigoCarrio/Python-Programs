"""
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)
*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B y viceversa:
    5. Verificacion de existencia de una letra del alfabeto.
    6. Salir.
Opcion: """)
    if opcion == "1":
        fu.list_alphabet(alfabeto_a)       
    elif opcion == "2":
        fu.list_alphabet(alfabeto_b)
    elif opcion == "3":
        fu.change_word(alfabeto_a,alfabeto_b)
    elif opcion == "4":
        fu.change_alphabetA_toalphabetB(alfabeto_a,alfabeto_b)
    elif opcion == "5":
        fu.check_word_in_alphabet(alfabeto_a,alfabeto_b)
    elif opcion == "6":
        break
    else:
        print("No ingresó una opcion.")