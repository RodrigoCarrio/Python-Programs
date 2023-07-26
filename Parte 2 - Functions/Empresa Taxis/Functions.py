'''
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_2   -   50
auto_3  -   chofer_3   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def view_driver(matriz):
    while True:
        driver = input("Ingrese nombre chofer: ").casefold()
        try:
            index = matriz[1].index(driver)
            if index >= 0:
                print(f"AUTO   -  RECORRIDO")
                print(f"{matriz[0][index]} -    {matriz[2][index]}  ")
        except:
            print("No existe el chofer")


def get_cars_by_route(matriz):
    while True:
        try:
            route = int(input("Ingrese la ruta del viaje: "))
        except:
            print("Error al ingresar el recorrido.")
        if route <= 0:
            print("La ruta debe ser mayor a 0.")
        else:
            print("Posibles autos y choferes que pueden realizar el viaje.")
            for i in range(len(matriz[2])):
                if(route <= matriz[2][i]):
                    print(f"Auto: {matriz[0][i]} - Chofer: {matriz[1][i]}")
        

def add_new_taxi(matriz):
    while True:
        car = input("Ingrese nuevo auto: ").casefold()
        driver = input("Ingrese el chofer del taxi: ")
        try:
            route = int(input("Ingrese el recorrido: "))
        except:
            print("Error al ingresar el recorrido.")
        if car not in matriz[0]:
            matriz[0].append(car)
            matriz[1].append(driver)
            matriz[2].append(route)
            break
        else:
            print("Auto ya registrado.")

def change_name_driver(matriz):
    while True:
        print("--------------CAMBIO DE NOMBRE-------------")
        car = input("Ingrese el auto a modificar el chofer: ")
        name = input("Ingrese el nombre del nuevo chofer:  ")
        if car == "1":
            matriz[1][0] = name
            break

        elif car == "2":
            matriz[1][1] = name
            break

        elif car == "3":
            matriz[1][2] = name
            break

        else:
            print("Ingresó un auto incorrecto.")

def change_name_driver2(matriz):
    while True:
        car = input("Ingrese el auto para modificar el chofer: ")
        try:
            index = matriz[0].index(car)
            matriz[1][index] = input("Ingrese nuevo nombre: ")
            break
        except:
            print("No existe el auto.")

def list_taxis(matriz):
    print("AUTO   -   CHOFER    - RECORRIDO")
    for i in range(len(matriz[0])):
        print(f"{matriz[0][i]} -   {matriz[1][i]}  -    {matriz[2][i]}")

def change_route(matriz):
    while True:
        print("--------------CAMBIO DE RUTA-------------")
        car = input("Ingrese el auto para modificar recorrido: ")
        try:
            route = int(input("Ingrese el recorrido nuevo: "))
        except:
            print("Error al ingresar recorrido nuevo.")

        if (car == "1") and (route > 0):
            matriz[2][0] = route
            break

        elif (car == "2") and (route > 0):
            matriz[2][1] = route
            break

        elif (car == "3") and (route > 0):
            matriz[2][2] = route
            break

        else:
            print("Ingresó un auto incorrecto o rutas menores a 0.")

#add_new_taxi(Taxis)
#list_taxis(Taxis)
#get_cars_by_route(Taxis)
#view_driver(Taxis)
change_name_driver2(Taxis)
list_taxis(Taxis)