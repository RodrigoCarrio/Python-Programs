"""
El programa dbe:
* pedir por teclado el dinero actual de una persona
* pedir por teclado el precio del insumo que quiere comprar en USD
* convertir ese dinero a USD (1USD -> $170)
* devolver por pantalla True en caso que pueda comprar. False en caso que no.
* No deben aparecer errores.
"""

while True:
    try:
        dinero_persona = float(input("Ingrese su dinero actual: "))
        precio_insumo_usd = float(input("Ingrese el precio del insumo en USD: "))
        valor_usd = 170
        convertir = dinero_persona / valor_usd
        if (convertir >= precio_insumo_usd):
            print(f"True. Puede comprar el insumo de { round(precio_insumo_usd,2) }USD con el dinero que posee que es de ${ round(convertir,2) }.")
            break
        else:
            print(f"False. Posee ${ round(convertir,2) } y no llega a comprar el insumo de { round(precio_insumo_usd,2) }USD. ")
            break
    except:
        print("Error")