"""
El programa debe:
*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    no deben generar errores
"""
flag = True
while flag:
    try:
        personas = int(input("Ingrese la cantidad de personas: "))
        if personas != 0:            
            edad_mayor = 1
            for i in range(personas):
                edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
                if edad > edad_mayor:
                    edad_mayor = edad
                else:
                    continue
            print(f"La persona con mayor edad es de: {edad_mayor} ")
        else:
            print("Ingrese cantidades mayores a 0")
    except:
        print("Error")