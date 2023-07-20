"""
El programa debe:
* contar con 4 funciones: suma, resta, multiplicacion y division
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 numeros para operar y devolver el resultado al usuario    
* no deben generar errores
"""

def suma(a,b):
    suma = a + b
    return suma

def resta(a,b):
    resta = a - b
    return resta

def multiplicacion(a,b):
    multiplicacion = a * b
    return multiplicacion

def division(a,b):
    try:
        if b==0:
            b=int(input("Ingrese un numero distinto de 0: "))
            return a / b
        else:
            print("Hola")
            division = a / b
            return division
    except:
        print("Error")

def pedir_numeros():
    while True:
        try:
            num_1 = int(input("Ingrese primer numero: "))
            num_2 = int(input("Ingrese segundo numero: ")) 
            break           
        except:
            print("Error") 
    return num_1,num_2

