"""
Crear una clase de Figura_Geometrica:
    * Cuyo constructor debe inicializar los atributos: tipo_de_figura, color, tamaño = pequeño
    * Se deben crear 3 metodos en la clase:
        1. Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
        2. Cambiar color de figura e indicar nuevo color.
        3. Verificar si la figura es tamaño pequeño, agrandar a tamaño grande. return True o False si es el tamaño del parametro.
"""
from Class_Figure import Geometrical_Figure as gm
import Functions as fu

while True:
    opcion = input("""
Ingrese una opcion:
1- Crear Figura
2- Presentar figuras
3- Cambiar color
4- Salir
Opcion: """)
    if opcion == "1":
        fu.create_figure()       
    elif opcion == "2":
        fu.view_figures()
    elif opcion == "3":
        nuevo_color = fu.change_color()
        gm.modify_color(nuevo_color)
    elif opcion == "4":
        break
    else:
        print("No ingresó una opcion.")