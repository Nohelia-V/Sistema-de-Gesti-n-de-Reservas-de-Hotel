#Validaciones
def validar_Codigo(codigo):
    if codigo.strip() == "":
        incorrecto = True
    else:
        incorrecto = False
    return incorrecto 

#Validar nombre que no este vacio
def validar_Nombre(nombre):
    if nombre.strip() == "":
        incorrecto = True
    else:
        incorrecto = False
    return incorrecto

#Validar que las noches sean mayor que cero
def validar_Noches(noches):
    if noches <= 0:
        incorrecto = True
    else:
        incorrecto = False
    return incorrecto

#validar valor xd
def validar_Valor(valor):
    if valor <= 0:
        incorrecto = True
    else:
        incorrecto = False
    return incorrecto


#Opcion 6 Menu
def mostrar_Estadisticas(lista_Reserva):
    if len(lista_Reserva) == 0:
        print("No existen reservas")
        return
    total_Reservas = len(lista_Reserva)
    ingresos_Totales = 0
    mayor = lista_Reserva[0]["Valor"]
    for reserva in lista_Reserva:
        ingresos_Totales += reserva["Total"]
        if reserva["Valor"] > mayor:
            mayor = reserva["Valor"]
    promedio = ingresos_Totales / total_Reservas

    print("-----Estadisticas Finales-----") 
    print("------------------------------")
    print(f"Cantidad total de reservas: {total_Reservas}")
    print(f"Ingresos Totales: {ingresos_Totales}")
    print(f"Reserva mayor: {mayor}")
    print(f"Promedio de Ingreso por Reservas: {promedio}")
    print("------------------------------")


#Opcion 5 Menu
def mostrar_Reserva(lista_Reserva):
    if len(lista_Reserva) == 0:
        print("No existen reservas")
        return
    for i in range(len(lista_Reserva)):
        print(f"Reserva {i+1}")
        print("______________________________")
        print(f"Codigo: {lista_Reserva[i] ["Codigo"]}")
        print(f"Nombre: {lista_Reserva[i] ["Nombre"]}")
        print(f"Noches: {lista_Reserva[i] ["Noches"]}")
        print(f"Valor por Noche: {lista_Reserva[i] ["Valor"]}")
        print(f"Total: {lista_Reserva[i] ["Total"]}")
        print(f"Categoria: {lista_Reserva[i] ["Categoria"]}")
        print("______________________________")


#Opcion 4 Menu
def eliminar_Reserva(lista_Reserva):
    solicitar_Codigo = str(input("Ingrese codigo a buscar: ")).strip()
    if validar_Codigo (solicitar_Codigo):
        print("El codigo no puede estar vacio!!!")
        return
    busqueda_Reserva = buscar_Reserva_Codigo(solicitar_Codigo, lista_Reserva)
    if busqueda_Reserva == None:
        print("Reserva no Existe!!")
        return
    lista_Reserva.remove(busqueda_Reserva)
    print("Se elimino correctamente!!")


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