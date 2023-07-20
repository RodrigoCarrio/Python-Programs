"""
El programa debe:
* contar con 4 funciones: area(cuadrado), perimetro(cuadrado), area(circulo) y perimetro(circulo)
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 parametros y devolver el resultado al usuario    
* gestionar posibles errores
"""
from numpy import pi

def area_cuadrado():
    while True:
        try:
            a = int(input("Ingrese un numero para calcular el area en metros: "))
            if (a<=0):
                print("Ingrese numero mayor a 0")
            else:
                print(f"El area de un cuadrado de {a} x {a} = {a*a} m2 ")
                break
        except:
            print("Error. Ingrese un numero")

def perimetro_cuadrado():
    while True:
        try:
            a = int(input("Ingrese un numero para calcular el perimetro en metros: "))
            if (a<=0):
                print("Ingrese numero mayor a 0")
            else:
                for i in range(4):
                    print(f"El lado {i+1} es de {a} m2 ")
                print(f"El perimetro del cuadrado es de {a*4} m2")
        except:
            print("Error. Ingrese un numero")

def area_circulo():
    while True:
        try:
            a = int(input("Ingrese el radio del circulo para calcular el area: "))
            if (a<=0):
                print("Ingrese numero mayor a 0")
            else:
                print(f"El area del circulo con un radio de {a} es = {round(pi*(a**2),2)} ")
        except:
            print("Error. Ingrese un numero")

def perimetro_circulo():
    while True:
        try:
            radio = int(input("Ingrese el radio del circulo : "))
            if (radio<=0):
                print("El radio debe ser mayor a 0")
            else:
                print(f"El perimetro del circulo es igual a {round(2*pi*radio,2)} ")
                break
        except:
            print("Error. Ingrese numeros")

