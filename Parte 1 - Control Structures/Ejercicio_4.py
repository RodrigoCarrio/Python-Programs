"""
El programa debe:
* pedir en orden el nombre, apellido, edad y numero de calzado
* verificar que cada uno sea el tipo de variable correcto (importante)
* en caso verdadero imprimir de la siguiente manera el resultado
Example
Nombre: Lionel
Apellido : Messi
Edad: 34
Numero de calzado: 42.5
* caso contrario imprimir error
"""

while True:    
    nombre = input("Ingrese nombre: ").capitalize()
    apellido = input("Ingrese apellido: ").capitalize()
    if nombre.isalpha() and apellido.isalpha():
        try:    
            edad = int(input("Ingrese edad: "))
            calzado = float(input("Ingrese numero de calzado: "))
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Edad: {edad}")
            print(f"Numero de calzado: {calzado}")
            break
        except:
            print("Error. Ingreso algun dato incorrecto.")
    else:
        print("Error.No ingreso letras para el nombre y/o el apellido.")
        
