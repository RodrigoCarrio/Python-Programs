"""
Crear una funcion que debe: (usar diccionario): 
    * Contener un diccionario con distintas monedas de paises, siendo: La key el nombre de la moneda y el valor el simbolo.
    * Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe.
"""
currency = {
    "Peso" : "$",
    "Dolar" :  "US$",
    "Euro" : "€"
}

def get_value(diccionario):
    while True:
        key = input("Ingrese la moneda que desea o 1 para salir: ").capitalize()
        if key == "1":
            break
        else:
            valor = diccionario.get(key,"No existe")
            print(f"El simbolo de {key} : {valor}")

get_value(currency)