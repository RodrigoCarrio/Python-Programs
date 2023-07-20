"""
El programa debe:
* Pedir al usuario un numero menor a 20 y una palabra alfabetica.
* Imprimir esa palabra la cantidad de veces segun el numero que ingreso el usuario
* No generar errores
"""
flag = True
while flag:
    try:
        numero = int(input("Ingrese un numero menor a 20: "))
        palabra = input("Ingrese una palabra: ")
        if (numero < 20) and (palabra.isalpha()) and (numero != 0):
            print(numero)
            i=1
            while i <= numero:
                print(f"{i},{palabra}")
                i = i + 1
            flag = False
        else:
            print("Error. El numero es mayor a 20 o igual a 0. O la palabra no es alfabetica.")
    except:
        print("Error.")