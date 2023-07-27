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
def check_word_in_alphabet(array_1,array_2):
    while True:
        print("--------------VERIFICAR LETRA EN ALFABETO-------------")
        word = str(input("Ingrese una letra a verificar: "))
        select = input("""Seleccione el alfabeto:
    1. Alfabeto A
    2. Alfabeto B     
    opcion: """)
        if select == "1":
            for i in array_1:
                if word == i:
                    print(f"La letra '{word}' se encuentra en el alfabeto A.")
                else:
                    print(f"No se encuentra la letra '{word}'en el alfabeto A")
            break
        elif select == "2":
            for i in array_2:
                if word in array_1:
                    print(f"La letra '{word}' se encuentra en el alfabeto B.")
                else:
                    print(f"No se encuentra la letra '{word}'en el alfabeto B")
            break
        else:
            print("Opcion incorrecta")
        

def list_alphabet(array):
    print("--------------LISTAR ALFABETO-------------")
    for i in array:
        print(i, end=" , ")
    print("")

def change_word(array_1,array_2):
    while True:
        print("--------------DUPLICACION DE LETRA-------------")
        word = input("Ingrese una letra del alfabeto A: ").casefold()
        try:
            index = array_1.index(word)
            array_1[index] = word+word
            array_2[index] = array_2[index]+array_2[index]
            print("Duplicacion exitosa")
            break
        except:
            print("No existe la letra ingresada.")

def change_alphabetA_toalphabetB(array_1,array_2):
    word = ""
    while True:
        print("--------------CAMBIO DE UN ALFABETO A OTRO Y VICEVERSA-------------")
        for i in range(len(array_1)):
            word = array_2[i]
            array_2[i] = array_1[i]
            array_1[i] = word
        print("Cambio exitoso")            
        break
