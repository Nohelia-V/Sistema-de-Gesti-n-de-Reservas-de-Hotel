#Validaciones

#Opcion 6 Menu
def mostrar_Estadisticas():
    pass
#Opcion 5 Menu
def mostrar_Reserva():
    pass
#Opcion 4 Menu
def eliminar_Reserva():
    pass
#Opcion 3 Menu
def actualizar_Reserva():
    pass
#Opcion 2 Menu
def buscar_Reserva():
    pass
#Opcion 1 Menu
def registrar_Reserva():
    pass
#Opciones Seleccionadas del Menu
def opcion_Menu():
    try:
        opcion =int(input("Seleccione una opcion: "))
        if opcion >=1 and opcion <=7:
            return opcion
        print("Opcion fuera de rango")
        return 0
    except ValueError:
        print("Ingrese solo numeros Enteros")
        return 0
#Muestro Menu Principal
def mostrar_Menu():
    print("---------Reserva Hotel---------")
    print("1. Registrar Reserva")
    print("2. Buscar Reserva")
    print("3. Actualizar Reserva")
    print("4. Eliminar Reserva")
    print("5. Mostrar Reserva")
    print("6. Mostrar Estadisticas")
    print("7. Salir")
    print("------------------------------------")
###################################################
def main ():
    pass
main()