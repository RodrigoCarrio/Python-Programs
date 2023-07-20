"""
El programa debe:
* Pedir al usuario una palabra
* verificar que sea una palabra
* mostrar por pantalla las letras una a una    
* no deben generar errores
"""
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra.isalpha():
        for i in palabra:
            print(i,end=",")
        break
    else:
        print("No ingreso una palabra")