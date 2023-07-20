"""
El programa debe:
* contar con 4 funciones: area(cuadrado), perimetro(cuadrado), area(circulo) y perimetro(circulo)
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 parametros y devolver el resultado al usuario    
* gestionar posibles errores
"""
import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
1- Area cuadrado
2- Perimetro cuadrado
3- Area Circulo
4- Perimetro Circulo
5- Salir
Opcion: """)
    if opcion == "1":
        fu.area_cuadrado()        
    elif opcion == "2":
        fu.perimetro_cuadrado()
    elif opcion == "3":
        fu.area_circulo()
    elif opcion == "4":
        fu.perimetro_circulo()
    elif opcion == "5":
        break
    else:
        print("No ingresó una opcion.")