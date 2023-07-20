"""
El programa debe:
* Pedir un dato numerico al usuario.
* imprimir la tabla del numero del 1 al 10.
* no generar errores
"""
flag = True
while flag:
    try:
        numero = int(input("Ingrese un numero: "))
        if numero != 0:
            i = 1
            while i <= 10:
                print(i*numero)
                i = i+1
            flag = False
        else:
            print("Ingreso 0.")
    except:
        print("Error")
