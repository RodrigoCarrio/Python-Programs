"""
El programa debe ser capaz de:
* Solicitar 2 argumentos al usuario
* imprimir por pantalla el resultado de la suma de ambos argumentos
"""
#Opcion 1
print("Suma de numeros")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = a + b
print(suma)

#Opcion 2
def suma(a,b):
    resultado = int(a) + int(b)
    print(f"La suma de {a} y {b} es igual a: {resultado}")

suma(a,b)

