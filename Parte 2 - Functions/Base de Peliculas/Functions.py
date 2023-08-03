"""
El programa debe:

* Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
* Debe comenzar con las siguientes peliculas y series en un diccionario:

base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

* Contar con 5 funciones disponibles en el menu:
    1- Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2- Agregar nuevas peliculas o series (que no esten) en la base.
    3- Eliminar peliculas o series de la base.
    4- Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
    5- Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el").
"""

def find_films_series_by_word(dictionary):
    while True:
        print(f"------- FILTRAR PELICULA O SERIE POR PALABRA -------")
        option = input("Ingrese la palabra 'peliculas' o 'series' para buscar informacion de ella: ").casefold()
        if option in dictionary:
            value = dictionary.get(option)
            word = input("Escriba lo que desea para encontrar. Si escribe un titulo ingrese la primer letra con mayuscula: ")
            for i in value:
                if word in i:
                    print(i)
            break
        else:
            print(f"No se encontro nada con la palabra '{option}'.")

def print_films_from_to(dictionary):
    while True:
        print(f"------- MOSTRAR PELICULAS -------")
        try:
            value = dictionary.get("peliculas")
            start = int(input("Ingrese un numero mayor a 0 desde donde quiere comenzar a filtrar las peliculas: "))
            end = int(input("Hasta que numero de peliculas quiere filtrar? Ingrese un numero mayor al comienzo: "))
            if (start > 0) and (end > start):
                if end > len(value):
                    for i in range(start-1,len(value)):
                        print(f"La {i+1}° pelicula  es: {value[i]}.")
                    break
                else:
                    for i in range(start-1,end):
                        print(f"La {i+1}° pelicula  es: {value[i]}.")
                    break
            else:
                print("Ingrese valores mayores a 0 y/o el numero desde donde quiere comenzar a filtrar debe ser menor que el de 'hasta'.  ")               
        except:
            print("Error")

def delete_films_series(dictionary):
    while True:
        print(f"------- ELIMINAR PELICULAS O SERIES -------")
        option = input("Ingrese la palabra 'peliculas' o 'series' para eliminar lo que desea de ella: ").casefold()
        if option in dictionary: 
            value = dictionary.get(option)
            film_serie = input(f"Escriba la {option} que desea eliminar: ").capitalize()
            if film_serie in value:
                value.remove(film_serie)
                print(f"Se elimino con exito la {option}: '{film_serie}'. ")
                break
            else:
                print(f"La {option} '{film_serie}' no se encuentra.")
        else:
            print(f"La palabra ingresada '{option}' no encuentra nada.")

def print_films_series(dictionary):
    while True:
        print(f"------- IMPRIMIR PELICULAS O SERIES -------")
        option = input("Ingrese la palabra 'peliculas' o 'series' para ver su informacion: ").casefold()
        if option in dictionary:   
            value = dictionary.get(option)
            print(f"-------INFORMACION DE {option.upper()}-------")
            for i in value:
                print(i)
            break
        else:
            print(f"La palabra ingresada '{option}' no encuentra nada.")

def add_new_films_series(dictionary):
    while True:
        print(f"------- AGREGAR PELICULAS O SERIES -------")
        option = input("Ingrese la palabra 'peliculas' o 'series' para agregar nueva informacion: ").casefold()
        if option in dictionary:   
            value = dictionary.get(option)
            film_serie = input(f"Ingrese la nueva {option}: ").capitalize()
            if film_serie in value:
                print(f"La '{film_serie}' ya se encuentra en la lista. Agregue otra nueva.")
            else:
                value.append(film_serie)
                print(f"Se agregó con exito la {option}: '{film_serie}'. ")
                break
        else:
            print(f"La palabra ingresada '{option}' no encuentra nada.")
