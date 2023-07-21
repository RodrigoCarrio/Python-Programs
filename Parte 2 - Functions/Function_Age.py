"""
Crear una funcion
* Que pida al usuario una cantidad de personas
* Pedir al usuario uno a uno la edad de las personas
* Finalizado la carga de las edades, imprimir por pantalla la edad mayor    
* gestionar posibles errores
"""

edad_personas = []

def pedir_edades():
    while True:
        try:
            personas = int(input("Ingrese cantidad de personas: "))
            if personas <= 0:
                print("Ingrese cantidades mayores a 0.")
            else:
                for i in range(personas):
                    flag_1 = True
                    while flag_1:
                        edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
                        if edad < 0:
                            print("Ingrese edades mayores a 0")
                        else:
                            edad_personas.append(edad)
                            print(f"Ingresó {edad} años.")
                            flag_1 = False
                print(f"La edad mas grande es {max(edad_personas)} años. ")
        except:
            print("Error")

pedir_edades()