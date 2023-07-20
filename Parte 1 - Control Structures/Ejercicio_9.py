"""
El programa debe: 
* pedir al usuario que ingrese una palabra.
* verificar que la palabra ingresada esté en minuscula o mayuscula.
* Imprimir posibles errores.
"""

while True:
    palabra = input("Ingrese una palabra: ")
    if palabra.isalpha():
        if palabra.islower():
            print("La palabra que ingresos está en minuscula.")
            break
        elif palabra.isupper():
            print("La palabra que ingresó se encuentra en mayusculas")
            break
        else:
            print("La palabra contiene ambas formas, mayusculas y minusculas")
            break
    else:
        print("Error. Ingrese solo letras.")