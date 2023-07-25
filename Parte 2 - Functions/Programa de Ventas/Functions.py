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
base_productos = [[1,2,3], ["producto1", "producto2", "producto3"], [300,400,500], [5,4,7]]

def agregar_stock(matriz):
    while True:
        print("--------------AGREGAR STOCK-------------")
        codigo = input("Ingrese el codigo del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
        except:            
            print("Error al cargar una cantidad.")

        if (codigo == "1") and (cantidad > 0):           
            matriz[3][0] += cantidad
            print(f"Se actualizo el stock a {matriz[3][0]} ")
            break

        elif (codigo == "2") and (cantidad > 0):
                matriz[3][1] += cantidad
                print(f"Se actualizo el stock a {matriz[3][1]} ")
                break

        elif (codigo == "3") and (cantidad > 0):
                matriz[3][2] += cantidad
                print(f"Se actualizo el stock a {matriz[3][2]} ")
                break 
        else:
            print("Opcion incorrecta y/o cantidad menor a 0.")

def cambiar_precio(matriz):
    while True:
        print("--------------CAMBIO DE PRECIO-------------")
        codigo = input("Ingrese el codigo del producto: ")
        try:
            precio_nuevo = int(input("Ingrese el precio nuevo: "))
        except:            
            print("Error al cargar un precio nuevo.")

        if (codigo == "1") and (precio_nuevo > 0):
            matriz[2][0] = precio_nuevo
            print(f"Precio actualizado a ${precio_nuevo}.")
            break

        elif (codigo == "2") and (precio_nuevo > 0):
            matriz[2][1] = precio_nuevo
            print(f"Precio actualizado a ${precio_nuevo}.")
            break

        elif (codigo == "3") and (precio_nuevo > 0):
            matriz[2][2] = precio_nuevo
            print(f"Precio actualizado a ${precio_nuevo}.")
            break  

        else:
            print("Opcion incorrecta y/o cantidad menor a 0.")
        
def tarjeta_credito(matriz):
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(matriz[1])):
            print(f"{matriz[0][i]}  {matriz[1][i]}")
            
        try:
            producto = int(input("Ingrese el codigo del producto: "))
            if producto == 1:
                for i in range(2,len(matriz)-1):
                    for j in matriz[i]:                    
                        if j == matriz[i][0]:
                            suma = j + (j*0.10)
                            break
                    break

                for i in range(3,len(matriz)):
                    for j in matriz[i]:
                        if j == matriz[i][0]:
                            matriz[i][0] = matriz[i][0] - 1
                            print("Se desconto del stock.")
                            break
                    break
                return suma

            elif producto == 2:
                for i in range(2,len(matriz)-1):
                    for j in matriz[i]:                    
                        if j == matriz[i][1]:
                            suma = j + (j*0.10)
                        else:
                            continue
                    break
                
                for i in range(3,len(matriz)):
                    for j in matriz[i]:
                        if j == matriz[i][1]:
                            matriz[i][1] = matriz[i][1] - 1
                            print("Se desconto del stock.")
                            break
                    break
                return suma

            elif producto == 3:
                for i in range(2,len(matriz)-1):
                    for j in matriz[i]:                    
                        if j == matriz[i][2]:
                            suma = j + (j*0.10)
                        else:
                            continue
                    break

                for i in range(3,len(matriz)):
                    for j in matriz[i]:
                        if j == matriz[i][2]:
                            matriz[i][2] = matriz[i][2] - 1
                            print("Se desconto del stock.")
                            break
                    break
                return suma
            else:
                print("Opcion incorrecta")                            
        except:
            print("Error")

def mostrar_menu(matriz):
    print("Cod.      Producto      Precio    Stock")
    for i in range(len(matriz)-1):
        print(f"{base_productos[0][i]}            {base_productos[1][i]}        {base_productos[2][i]}        {base_productos[3][i]} ")

def mostrar_menu2(matriz):
    print("Cod     Producto      Precio   Stock")
    for i in range(len(matriz)-1):
        if i !=0:
            print("")
        for j in range(len(matriz)):
            print(f"{matriz[j][i]}",end="\t")
        print("")

def mostrar_menu_productos(matriz):
    print("Cod     Producto")
    for i in range(len(matriz)-1):
        if i !=0:
            print("")
        for j in range(2):
            print(f"{matriz[j][i]}",end="\t")
    

def forma_pago():
    while True:
        opcion = input("""
    Ingrese un metodo de pago
1. Efectivo
2. Tarjeta Debito
3. Tarjeta Credito
opcion: """)
        if opcion == "1":
            return "Efectivo"
        elif opcion == "2":
            return "Debito"
        elif opcion == "3":
            return "Credito"
        else:
            print("Opcion incorrecta.")



def pagar_con_credito2(matriz):
    print(f"--------------PAGO CON CREDITO-------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(matriz[1])):
            print(f"{matriz[0][i]}  {matriz[1][i]}")
        opcion=input("--> ")        
        if opcion=="1":
            if(matriz[3][0]>0):
                matriz[3][0]=matriz[3][0]-1 #resto stock
                suma = matriz[2][0] + (matriz[2][0] *0.1)
                #print(f"El comprador debe pagar:$ {matriz[2][0]*1.1}")
                return suma 
            else:
                print("No hay stock")
        elif opcion=="2":
            if(matriz[3][1]>0):
                matriz[3][1]=matriz[3][1]-1 #resto stock
                suma = matriz[2][1] + (matriz[2][1] *0.1)
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][1]*1.1}")
                return suma
            else:
                print("No hay stock")
        elif opcion=="3":
            if(matriz[3][2]>0):
                matriz[3][2]=matriz[3][2]-1 #resto stock
                suma = matriz[2][2] + (matriz[2][2] *0.1)
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][2]*1.1}")
                return suma
            else:
                print("No hay stock")
        else:
            print("No ingreso una opcion correcta")

def pagar_debito(matriz):
    print(f"--------------PAGO CON DEBITO-------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(matriz[1])):
            print(f"{matriz[0][i]}  {matriz[1][i]}")
        opcion=input("--> ")        
        if opcion=="1":
            if(matriz[3][0]>0):
                matriz[3][0]=matriz[3][0]-1 #resto stock
                #print(f"El comprador debe pagar:$ {matriz[2][0]*1.1}")
                return matriz[2][0] 
            else:
                print("No hay stock")
        elif opcion=="2":
            if(matriz[3][1]>0):
                matriz[3][1]=matriz[3][1]-1 #resto stock
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][1]*1.1}")
                return [2][1]
            else:
                print("No hay stock")
        elif opcion=="3":
            if(matriz[3][2]>0):
                matriz[3][2]=matriz[3][2]-1 #resto stock
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][2]*1.1}")
                return matriz[2][2]
            else:
                print("No hay stock")
        else:
            print("No ingreso una opcion correcta")

def pagar_efectivo(matriz):
    print(f"--------------PAGO CON CREDITO-------------")
    while True:
        print(f"Que producto desea vender:")
        for i in range(len(matriz[1])):
            print(f"{matriz[0][i]}  {matriz[1][i]}")
        opcion=input("--> ")        
        if opcion=="1":
            if(matriz[3][0]>0):
                matriz[3][0]=matriz[3][0]-1 #resto stock
                suma = matriz[2][0] - (matriz[2][0] *0.1)
                #print(f"El comprador debe pagar:$ {matriz[2][0]*1.1}")
                return suma 
            else:
                print("No hay stock")
        elif opcion=="2":
            if(matriz[3][1]>0):
                matriz[3][1]=matriz[3][1]-1 #resto stock
                suma = matriz[2][1] - (matriz[2][1] *0.1)
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][1]*1.1}")
                return suma
            else:
                print("No hay stock")
        elif opcion=="3":
            if(matriz[3][2]>0):
                matriz[3][2]=matriz[3][2]-1 #resto stock
                suma = matriz[2][2] - (matriz[2][2] *0.1)
                #print(f"El comprador debe pagar:$ {vr.base_productos[2][2]*1.1}")
                return suma
            else:
                print("No hay stock")
        else:
            print("No ingreso una opcion correcta")

mostrar_menu2(base_productos)
agregar_stock(base_productos)
mostrar_menu2(base_productos)