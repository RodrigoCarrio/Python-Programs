"""
Crear una funcion que debe:
*    Tener almacenado el abecedario en una lista
*    Pedir al usuario un numero (2 o 3).
*    Eliminar de la lista las letras que ocupen posiciones multiplos de ese numero.
*    Mostrar por pantalla la lista resultante
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def delete_words():
    while True:
        try:
            number = int(input("Input the number 2 or 3: "))
            if (number == 2) or (number == 3):
                for i in range(0,26,1):
                    print("Entre")
                    abecedario.pop(i)
                print(abecedario)
            else:
                print("Entre al else")
        except:
            print(abecedario)
            print("Error")

delete_words()