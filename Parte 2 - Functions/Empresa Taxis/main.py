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
import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
1. Preguntar recorrido de viaje e indicar posibles autos y choferes.
2. Modificar nombre chofer segun el nombre del auto.
3. Modificar el recorrido segun el nombre del auto.
4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo.
5. Mostrar lista de autos choferes y recorrido maximo.
6. Observar informacion de un chofer.
7. Salir.
Opcion: """)
    if opcion == "1":
        fu.get_cars_by_route(Taxis)       
    elif opcion == "2":
        fu.change_name_driver2(Taxis)
    elif opcion == "3":
        fu.change_route(Taxis)
    elif opcion == "4":
        fu.add_new_taxi(Taxis)
    elif opcion == "5":
        fu.list_taxis(Taxis)
    elif opcion == "6":
        fu.view_driver(Taxis)
    elif opcion == "7":
        break
    else:
        print("No ingresó una opcion.")