"""
El programa debe:
* pedir un numero al usuario entero positivo
* Mostrar por pantalla la cuenta atras desde ese numero hasta 0 por comas.
"""
flag = True
while flag:
    try:
        numero = int(input("Ingrese un numero: "))
        if numero == 0:
            print("Ingresó 0")
        else:
            for i in range(numero,0-2,-2):
                print (i,end=",")
            flag = False
    except:
        print("Error")