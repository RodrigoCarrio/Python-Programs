from Class_Figure import Geometrical_Figure as gm

geometrical_figures = []

def create_figure():
    #TYPE FIGURE
    while True:
        type_figure = input("Ingrese el tipo de figura: ").capitalize()
        if type_figure.isalpha():
            break
        else:
            print("Ingrese palabras unicamente")

    #COLOR
    while True:
        color = input("Ingrese el color de figura: ").capitalize()
        if color.isalpha():
            break
        else:
            print("Ingrese palabras unicamente.")

    #CREATE OBJECT
    instance = gm(type_figure, color)
    geometrical_figures.append(instance)

def view_figures():
    for i in geometrical_figures:
        i.introduce()

def change_color():
    while True:
        new_color = input("Ingrese el color nuevo: ")
        if new_color.isalpha():
            return new_color
        else:
            print("Ingrese una palabra.")
