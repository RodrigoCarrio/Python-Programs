"""
Crear una funcion que debe: (usar set)
* Pedir al usuario determinados paises y guardarlos en un set
* Cuando el usuario escriba "listo", se debe imprimir todos los paises sin repetir, y la cantidad total sin repetir
"""

paises = set()
while True:
    pais = input("Ingrese un pais o escriba 'listo' para salir: ").capitalize()
    if pais.isalpha():
        if pais == "Listo":
            break
        paises.add(pais)
    else:
        print("Error.")
   
for i in paises:
    print(i)
print(f"En total se cargaron {len(paises)} sin repetir.")
print(type(paises))