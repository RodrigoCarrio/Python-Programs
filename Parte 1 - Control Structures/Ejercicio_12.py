"""
El programa debe:
* Permitir al usuario ingresar un numero menor a 20.
* Imprimir tantas veces hasta llegar al numero que ingreso.
"""
flag = True
while flag:
    try:
        numero = int(input("Ingrese un numero menor a 20: "))
        if (numero < 20) and (numero != 0):
            i = 1
            while i <= numero:
                print(f"Iteracion {i}.")
                i = i + 1
            flag = False
        else:
            print("Error. Ingreso un numero mayor a 20 o ingreso 0.")
    except:
        print("Error")

