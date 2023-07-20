"""
El programa debe:
* contar con 4 funciones:
    1. Conversor de Grados Celcius a Fahrenheit.
    2. Conversor de cm3 a litros
    3. Conversor de litros a cm3.
    4. Pesos a USD
* contar con un menu donde debe pedir al usuario que realizar
* pedir los 2 parametros y devolver el resultado al usuario    
* gestionar posibles errores
"""

def celcius_a_fahrenheit(c):
    try:
        c = int(c)
        fahrenheit = (c * 1.8) + 32
        return fahrenheit
    except:
        print("Error")


def cm3_a_litros(c):
    try:
        c = int(c)
        litros = c / 1000
        return litros
    except:
        print("Error")

def litros_a_cm3(c):
    try:
        c = int(c)
        cm3 = c * 1000
        return cm3
    except:
        print("Error")

def pesos_a_usd(c):
    try:
        c = int(c)
        dolar = c / int(input("Ingrese la equivalencia de USD: "))
        return dolar
    except:
        print("Error")

