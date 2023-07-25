"""
Crear un programa que debe:
* Simular un programa que calcule estadisticas
* Pedir al usuario una serie de numeros enteros del 1 al 10 y guardarlos en una lista hasta que el usuario ingrese "fin".
* Mostrar un menu con 4 opciones
    1. Calcular promedio
    2. Verificar cuantos numeros son menores que el numero indicado por el usuario
    3. Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
    4. Verifica si un numero que desee el usuario está en la lista.
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""

numbers = []

def pedir_numeros():
    while True:        
        number = input("Ingrese numeros del 1 al 10 o fin: ")
        if number == "fin":
            break
        elif number.isdigit():            
            number = int(number)
            if (number <= 0) or (number > 10):
                print("Ingrese numeros entre 1 y 10.")
            else:
                numbers.append(number)
                print(f"Se agregó el numero {number}.")
        else:
            print("Error")

def calcular_promedio():
    print(numbers)
    promedio = 0
    for i in range(0,len(numbers)):
        promedio += numbers[i]        
    print(f"El promedio es igual a {round(promedio/(len(numbers)),2)}. ")

def verificar_numero():
    while True:
        try:
            number = int(input("Ingrese un numero para verificar si está en la lista: "))
            if number in numbers:
                print(f"El numero {number} se encuentra en la lista.")
                break
            else:
                print(f"El numero {number} no se encuentra en la lista.")
                break
        except:
            print("Error al ingresar un numero.")

def verificar_numeros_menores():
    while True:
        try:
            number = int(input("Ingrese un numero a comparar: "))
            numbers.sort()
            contador = 0
            for i in numbers:
                if i < number:
                    contador += 1
                    print(f"Numero {i}")
            print(f"La cantidad de numeros menores antes de '{number}' es de {contador} ")
            break
        except:
            print("Error al ingresar un numero")

def verificar_numeros_mayores():
    while True:
        try:
            number = int(input("Ingrese un numero a comparar: "))
            numbers.sort()
            contador = 0
            for i in numbers:
                if i > number:
                    contador += 1
                    print(f"Numero {i}")
            print(f"La cantidad de numeros mayores despues de '{number}' es de {contador}. ")
            break
        except:
            print("Error al ingresar un numero")
