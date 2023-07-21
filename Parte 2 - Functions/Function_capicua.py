"""
Crear una funcion que debe:
* Que pida al usuario una palabra o frase
* Indicar si esta se trata de un palindromo/capicua (neuquen, reconocer, amor a roma.)    
* gestionar posibles errores
"""

def palindromo():
    palabra_frase = input("Ingrese una palabra: ")  
    original = list(palabra_frase)
    reversa = original.copy()
    reversa.reverse()
    if original == reversa:
        print("Ok es igual")
    else:
        print("No es capicua")

palindromo()