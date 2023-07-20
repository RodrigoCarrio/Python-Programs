"""
El programa debe:
* Mostrar al usuario un menu
* Permitir al usuario ingresar una opcion del menu
* imprimir esa opcion
en caso de no escribir ninuna opcion del menu indicar ERROR
Condiciones:

imprimir (string)
1 (int)
2 (int)
salir (string)
Ayuda (como se comparan string y enteros cuidado con castear antes de verificar si el usuario ingreso str o int)
"""

while True:
    try:
        opcion = input("""
---------- MENU ----------
Por favor ingrese una opcion:
- IMPRIMIR
- 1
- 2
- SALIR
Ingresó: """)
        if opcion.isalpha():
            opcion = opcion.upper()
            if opcion == "IMPRIMIR":
                print("Hola me llamaste a imprimir.")
                break
            elif opcion == "SALIR":
                print("Voy a salir")
                break
            else:
                print("Ingresó cualquier palabra.")

        elif opcion.isdigit():
                opcion = int(opcion)
                if opcion == 1:
                    print(f"Soy", opcion)
                    break
                elif opcion == 2:
                    print(f"Soy", opcion)
                    break
                else:
                    print("Ingresó cualquier numero.")
        else:
            print("ingresó ni numeros ni palabras")
    except: 
        print("Error")


