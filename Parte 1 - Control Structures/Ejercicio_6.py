"""
El programa debe:
* pedir al usuario 3 notas de 3 parciales diferentes.
* verificar que los datos ingresados sean correctos.
* En caso correcto imprimir el promedio
* Si no son correctos imprimir un error.
"""

while True:
    try:
        nota_1 = int(input("Ingrese una nota del 1 al 10: "))
        nota_2 = int(input("Ingrese la segunda nota del 1 al 10: "))
        nota_3 = int(input("Ingrese la tercer nota del 1 al 10: "))
        if (nota_1 and nota_2 and nota_3) <= 10:
            promedio = (nota_1 + nota_2 + nota_3) / 3
            print(f"El promedio de las notas ingresadas es igual a {(nota_1 + nota_2 + nota_3) / 3}.")
            break
        else:
            print("No ingreso notas entre 1 y 10.")
    except:
        print("Error")