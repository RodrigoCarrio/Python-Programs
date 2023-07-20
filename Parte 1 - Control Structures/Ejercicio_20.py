"""
El programa debe:
*    Pedir al usuario una cantidad de tramos de un viaje
*    Pedir al usuario la duración en minutos de cada tramo
*    Calcular el tiempo total de viaje
*    No deben generar errores
"""
from numpy import arange
flag = True
while flag:
    try:
        tramos_viaje = int(input("Ingrese la cantidad de tramos que tiene su viaje: "))
        if tramos_viaje == 0:
            print("Ingrese tramos de viaje superiores a 0")
        else:            
            tiempo_total_viaje = 0
            for i in arange(tramos_viaje):
                duracion_minutos = float(input(f"Ingrese la duracion en minutos del tramo {i+1}:  "))
                tiempo_total_viaje = tiempo_total_viaje + duracion_minutos
            print(f"El tiempo total de viaje fue de {tiempo_total_viaje} minutos.")
            flag = False
    except:  
        print("Error")