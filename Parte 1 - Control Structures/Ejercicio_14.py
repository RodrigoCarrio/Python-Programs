"""
El programa debe:
* Pedir al usuario 5 datos numericos.
* verificar que sean enteros y sino pedir nuevamente los 5.
* devolver el promedio 
* no generar errores
"""

flag = True
while flag:
    try:
        dato_1 = int(input("Ingrese el primer dato numerico: "))
        dato_2 = int(input("Ingrese el segundo dato numerico: "))
        dato_3 = int(input("Ingrese el tercer dato numerico: "))
        dato_4 = int(input("Ingrese el cuarto dato numerico: "))
        dato_5 = int(input("Ingrese el quinto dato numerico: "))
        promedio = (dato_1 + dato_2 + dato_3 + dato_4 + dato_5) / 5
        print(f"El promedio es de {promedio} ")
        flag = False
    except:
        print("Error.")