from Class_people import Persona

peoples = []

def create_person():
    #DNI
    while True:
        dni = str(input("Ingrese el DNI de la persona: "))
        if (dni.isdigit()):
            flag = True
            for i in peoples:
                if i.dni == dni:
                    print("Ese DNI ya existe.")
                    flag = False
                    break
                else:
                    continue
            if (flag):
                break
        else:
            print("El dni no es numerico.")
    # NAME
    nombre = input("Ingrese el nombre de la persona: ").capitalize()

    # LAST NAME
    apellido = input("Ingrese el apellido de la persona: ").capitalize()

    # AGE
    while True:
        try:
            edad = int(input("Ingrese la edad de la persona: "))
            if edad > 0:
                break
            else:
                print("Ingrese una edad mayor a 0")
        except:
            print("Error al ingresar una edad.")
    
    # RESIDENT
    residencia = input("Ingrese la residencia de la persona: ").capitalize()

    #CREANDO OBJETO PERSONA
    persona = Persona(dni, nombre, apellido, edad, residencia)
    peoples.append(persona)

def listar_personas():
    for i in peoples:
        i.presentarse()

def age_range(): 
    while True:
        dni = input("Ingrese el DNI de la persona: ")
        for i in peoples:
            if i.dni == dni:
                return i
        print(f"El dni:{dni} no se encuentra.")