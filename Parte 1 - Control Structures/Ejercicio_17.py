"""
El programa debe:
* preguntar al usuario por una frase y una letra
* mostrar por pantalla el numero de veces que aparece la letra en la frase
"""
flag = True
while flag:
    frase = input("Ingrese una frase: ").lower()
    letra = input("Ingrese la letra que quiere contar: ").lower()
    if frase.isalpha() and letra.isalpha():
        for i in frase:
            if i == letra:
                print(letra)
                flag = False                            
    else:
        print("No ingreso una frase alfabetica.")
