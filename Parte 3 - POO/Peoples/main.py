"""
Crear una clase de Persona:
* Cuyo constructor debe inicializar los atributos dni, nombre, apellido, edad, ciudad de residencia.
* Se deben crear 2 metodos en la clase:
    1. Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad de residencia}
    2. Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolescente (15 a 22), Joven (23 a 30), Mayor (31 en adelante), 
* Menu:
    1. Para crear personas
    2. Segun el nombre de persona indicar edad.
"""
from Class_people import Persona
import Functions as fu        

while True:
    opcion = input("""
Ingrese una opcion:
1- Crear Personas
2- Verificar rango edad
3- Listar Personas
4- Salir
Opcion: """)
    if opcion == "1":
        fu.create_person()       
    elif opcion == "2":
        Persona.age_person(fu.age_range())
    elif opcion == "3":
        fu.listar_personas()
    elif opcion == "4":
        break
    else:
        print("No ingresó una opcion.")