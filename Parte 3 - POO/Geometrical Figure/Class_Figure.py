"""
Crear una clase de Figura_Geometrica:
    * Cuyo constructor debe inicializar los atributos: tipo_de_figura, color, tamaño = pequeño
    * Se deben crear 3 metodos en la clase:
        1. Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
        2. Cambiar color de figura e indicar nuevo color.
        3. Verificar si la figura es tamaño pequeño, agrandar a tamaño grande.
"""

class Geometrical_Figure:
    def __init__(self, figure_type, color, size = "small"):
        self.figure_type = figure_type
        self.color = color
        self.size = size

    def introduce(self):
        print(f"Un {self.figure_type} de color {self.color} y tamaño {self.size} ")
    
    def modify_color(self, new_color):
        print(f"Se cambia de color {self.color} al nuevo color {new_color} ")
        self.color = new_color
    
    def check_size_and_change(self):
        if (self.size) == "small":
            self.size = "big"
        else:
            print(f"El tamaño de la figura es {self.size}.")