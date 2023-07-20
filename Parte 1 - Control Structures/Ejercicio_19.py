"""
El programa debe:
* preguntar al usuario una cantidad a invertir. 
* preguntar al usuario el interes anual y el numero de años
* mostrar por pantalla el capital cobrado en la inversión cada año que dura la inversión.
"""

from numpy import arange
try:
    inversion = float(input("Ingrese la cantidad a invertir: "))
    interes_anual = float(input("Ingrese el interes anual: "))/100
    años_inversion = float(input("Ingrese los años a invertir: "))
    for i in arange(1,años_inversion+1):
        inversion = inversion + (inversion * interes_anual)
        print(f"En el año {i} la inversion acumula un valor de : ${inversion}")
except:
    print("Error")