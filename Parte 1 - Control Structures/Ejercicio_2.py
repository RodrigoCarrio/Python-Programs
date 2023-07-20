"""
El programa debe ser capaz de:
* Solicitar 2 argumentos al usuario
* verificar que los 2 argumentos sean enteros y en caso contrario volver a solicitarlos
* dar al usuario 3 intentos para escribir los argumento en total, (en caso de equivocarse en a o en b se resta un intento)
* imprimir por pantalla el resultado de la suma de ambos argumentos
"""

def suma(a,b):
    resultado = a + b
    print(f"La suma de {a} + {b} es igual a: {resultado}.")

i=0
while (i<3):
    try:
        a = int(input("Ingrese el primer numero: "))
        print(f"Ingreso el numero:{a}")
        b = int(input("Ingrese el segundo numero: "))
        print(f"Ingreso el numero:{b}")
        print(f"Se finalizó la carga de numeros. Fue correcta.")
        break
    except:
        print("Error. No ingreso un numero")
        i = i + 1
        if (i == 3):
            print("Se le dió 3 intentos y los ingreso incorrectamente")

try:
    print("Calculando la suma...")
    suma(a,b)
except:
    print("No se puede hacer la suma")
    