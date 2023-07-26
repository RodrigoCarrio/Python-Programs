'''
El programa debe:
*   Simular un programa que venda 3 productos
Codigo      Nombre      PRecio  stock
    1      producto1    300     5
    2      producto2    400     4
    3      producto3    500     7

*   El menu debe mostrar los productos a comprar. 
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito
*   Contar con 7 funciones disponibles en el menu:
  1. Ver menu de productos (Formato: codigo - producto) 
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) 
  3.  Pagar con tarjeta debito (se debe descontar el stock)
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock) 
  5.  Consultar productos y stock 
  6.  Agregar stock a los productos 
  7.  Cambiar el precio a los productos
  
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import Functions as fu
base_productos = [[1,2,3], ["producto1", "producto2", "producto3"], [300,400,500], [5,4,7]]

def forma_pago():
    while True:
        fu.mostrar_menu2(base_productos)
        opcion = input("""
    Ingrese un metodo de pago
1. Ver menu productos
2. Tarjeta Credito
3. Tarjeta Debito
4. Efectivo
5. Consultar productos y stock
6. Agregar stock a los productos
7. Cambiar el precio a los productos
8. Salir
opcion: """)
        if opcion == "1":
            fu.mostrar_menu_productos(base_productos)
        elif opcion == "2":
            print(f"Debe pagar el total de {fu.pagar_con_credito2(base_productos)}")
        elif opcion == "3":
            print(f"Debe pagar el total de {fu.pagar_debito(base_productos)}")
        elif opcion == "4":
            print(f"Debe pagar el total de {fu.pagar_efectivo(base_productos)}")
        elif opcion == "5":
            fu.consultar_productos_stock(base_productos)
        elif opcion == "6":
            fu.agregar_stock(base_productos)
        elif opcion == "7":
            fu.cambiar_precio(base_productos)
        elif opcion == "8":
          break        
        else:
            print("Opcion incorrecta.")

forma_pago()