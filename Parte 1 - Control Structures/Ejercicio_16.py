"""
El programa debe:
* mostrar el eco de todo lo que el usuario introduzca hasta que escriba "salir" que terminará
* si el usuario ingresa "hola" o "chau", no debe mostrar el eco
"""

while True:
    usuario = input("Ingrese alguna palabra: ").lower()
    if usuario == "salir":
        print(f"Ingreso {usuario} por lo tanto se termina el bucle.")
        break
    elif (usuario == "hola") or (usuario == "chau"):
        print("jaja")
        continue
    else:
        print(f"La palabra ingresada es: {usuario} ")