"""
Crear una clase de Persona:
* Cuyo constructor debe inicializar los atributos nombre, apellido, edad, ciudad de residencia.
* Se deben crear 2 metodos en la clase:
    1. Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad de residencia}
    2. Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolescente (15 a 22), Joven (23 a 30), Mayor (31 a 50), Mas mayor (51 a 120)
* Menu:
    1. Para crear personas
    2. Segun el nombre de persona indicar edad.
"""
class Persona:
    nacionalidad = "Argentina"

    # CONSTRUCTOR
    def __init__(self,dni, nombre, apellido, edad, residencia):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.residencia = residencia

    def presentarse(self):
        print(f"Soy {self.nombre} {self.apellido}, tengo {self.edad} años y vivo en {self.residencia}, {Persona.nacionalidad}. ")

    def age_person(self):
        if (self.edad > 0 and self.edad <= 14):
            print(f"{self.edad} años, {self.nombre} es un niño.")
        elif (self.edad > 14 and self.edad <= 22):
            print(f"{self.edad} años, {self.nombre} es un adolescente.")
        elif (self.edad > 22 and self.edad <= 30):
            print(f"{self.edad} años, {self.nombre} es un joven.")
        elif (self.edad > 30):
            print(f"{self.edad} años, {self.nombre} es mayor.")