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
import Functions as fu
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["Prision break", "La casa de papel" , "Los simpsons"]
        }

while True:
    opcion = input("""
Ingrese una opcion:
1- Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
2- Agregar nuevas peliculas o series (que no esten) en la base.
3- Eliminar peliculas o series de la base.
4- Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
5- Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el").
6. Salir.
Opcion: """)
    if opcion == "1":
        fu.print_films_series(base)       
    elif opcion == "2":
        fu.add_new_films_series(base)
    elif opcion == "3":
        fu.delete_films_series(base)
    elif opcion == "4":
        fu.print_films_from_to(base)
    elif opcion == "5":
        fu.find_films_series_by_word(base)
    elif opcion == "6":
        break
    else:
        print("No ingresó una opcion.")