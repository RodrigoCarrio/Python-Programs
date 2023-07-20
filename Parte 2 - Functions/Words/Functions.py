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

def contador_letras(letra,palabra_frase):
    while True:
        if letra.isalpha() and (len(letra)==1):      
            contador = 0
            for i in palabra_frase:
                if i == letra:                
                    contador += 1
            print(f"Contiene {contador} {letra} ")
            break
        else:
            print("Error, debe ingresar solo una letra.")
            break 

def comparador_palabras():
    while True:
        palabra_1 = input("Ingrese 1° palabra: ")
        palabra_2 = input("Ingrese 2° palabra: ")
        if palabra_1.isalpha() and palabra_2.isalpha():
            if len(palabra_1) > len(palabra_2):
                print(f"La palabra {palabra_1} contiene mas letras que la palabra {palabra_2}, un total de {len(palabra_1)}.")
                break
            elif len(palabra_1) == len(palabra_2):
                print("Las 2 palabras contienen las mismas cantidad de letras.")
                break
            else:
                print(f"La palabra {palabra_2} contiene mas letras que la palabra {palabra_1}, un total de {len(palabra_2)}")
                break
        else:
            print("Ingrese palabras unicamente.")

def quitador_vocales():
    flag = True
    while flag:
        palabra_frase = input("Ingrese la palabra o frase: ")
        for i in palabra_frase:
            if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
                continue
            else:
                print(i,end="")
        flag = False
