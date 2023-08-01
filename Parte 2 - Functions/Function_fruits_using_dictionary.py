"""
Crear una funcion que debe: (usar diccionario)

    * Guardar en un diccionario los precios de las frutas de la tabla.
    * Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta.
    * Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
Fruta	Precio
banana	50
manzana	80
pera	100
naranja	30
"""
fruits = {
    "banana" : 50,
    "manzana" : 80,
    "pera" : 100,
    "naranja" : 30
}

def get_info_fruits():
    while True:
        fruit = input("Ingrese una fruta a buscar: ").casefold()
        if fruit in fruits:
            try:
                kilos = float(input("Ingrese los kilos para calcular el precio: "))
                if kilos > 0: 
                    value = fruits.get(fruit)
                    print(f"Los {kilos}kg de {fruit} sale: ${value*kilos}")
                else:
                    print("Deben ser kilos mayores a 0")
            except:
                print("Error al ingresar los kilos.")
        else:
            print("Fruta no encontrada.")

get_info_fruits()