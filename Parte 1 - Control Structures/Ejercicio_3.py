"""
Estos son los deportes de un polideportivo. ¿Pueden ir tres amigos si a uno le gusta el futbol, otro le gusta el basket o voley, pero el ultimo odia el voley?
"""
#Polideportivo
futbol = True
basket = True
voley = False

#Amigos
amigo_1 = futbol
amigo_2 = basket or voley
amigo_3 = not voley

print(amigo_1 and amigo_2 and amigo_3)


"""
Funcion round()
"""
from math import * 

radio = 10
area = pi * radio**2
print(f"El area total es de:{area}m2")
print(f"El area total es de:{round(area,2)}m2")
