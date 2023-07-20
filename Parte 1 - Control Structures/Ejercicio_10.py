"""
El programa debe: 
* almacenar una variable contraseña 
* preguntar al usuario por la contraseña.
* Imprimir por pantalla si la contraseña ingresada por el usuario es igual a la contraseña almacenada.
"""

contraseña = "auto.COVID.2020"
usuario = input("Ingrese la contraseña correcta: ")
if (usuario == contraseña):
    print("La contraseña ingresada es correcta.")
else:
    print("No coinciden las contraseñas")