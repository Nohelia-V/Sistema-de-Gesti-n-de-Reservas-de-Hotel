def calcular_Categoria(total):
    if total < 200000:
        categoria = "Economica"
    elif total < 500000:
        categoria = "Estandar"
    else:
        categoria = "Premium"
    return categoria
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
def actualizar_Reserva(lista_Reserva):
    solicitar_Codigo = str(input("Ingrese codigo a buscar: ")).strip()
    if validar_Codigo (solicitar_Codigo):
        print("El codigo no puede estar vacio!!!")
        return
    busqueda_Reserva = buscar_Reserva_Codigo(solicitar_Codigo, lista_Reserva)
    if busqueda_Reserva == None:
        print("Reserva no Existe!!")
        return
    
    print("¡¡Reserva Encontrada!!")
    print("______________________________")
    print(f"1. Nombre: {busqueda_Reserva ["Nombre"]}")
    print(f"2. Noches: {busqueda_Reserva ["Noches"]}")
    print(f"3. Valor por Noche: {busqueda_Reserva ["Valor"]}")
    print("______________________________")
    print("¿Que campo desea modificar?\n (Escriba Numero)")
    try:
        modificacion = int(input())
    except ValueError:
        print("¡¡¡Ingrese solo numeros!!!")
        return
    if modificacion == 1:
        nuevo_Nombre = str(input("Ingrese nuevo nombre: ")).strip()
        if validar_Nombre(nuevo_Nombre):
            print("El nombre no puede estar vacio")
            return
        busqueda_Reserva ["Nombre"] = nuevo_Nombre
        print("Nombre modificado con Exito!!")
    elif modificacion == 2:
        try: 
            nuevas_Noches = int(input("Ingrese nueva cantidad de noches: "))
        except ValueError:
            print("Solo ingrese numeros!!")
            return
        if validar_Noches(nuevas_Noches):
            print("Las noches deben ser mayor a 0")
            return
        busqueda_Reserva ["Noches"] = nuevas_Noches
        total = nuevas_Noches * busqueda_Reserva ["Valor"]
        busqueda_Reserva ["Total"] = total
        categoria = calcular_Categoria(total)
        busqueda_Reserva ["Categoria"] = categoria
    elif modificacion == 3:
        try: 
            nuevo_Valor = int(input("Ingrese nueva valor: "))
        except ValueError:
            print("Solo ingrese numeros!!")
            return
        if validar_Valor(nuevo_Valor):
            print("El valor deben ser mayor a 0")
            return
        busqueda_Reserva ["Valor"] = nuevo_Valor
        total = nuevo_Valor * busqueda_Reserva ["Noches"]
        busqueda_Reserva ["Total"] = total
        categoria = calcular_Categoria(total)
        busqueda_Reserva ["Categoria"] = categoria
    else:
        print("Opcion fuera de rango!!")
        return
#Opcion 2 Menu
def buscar_Reserva(lista_Reserva):
    solicitar_Codigo = str(input("Ingrese codigo a buscar: ")).strip()
    if validar_Codigo (solicitar_Codigo):
        print("El codigo no puede estar vacio!!!")
        return
    busqueda_Reserva = buscar_Reserva_Codigo(solicitar_Codigo, lista_Reserva)
    if busqueda_Reserva == None:
        print("Reserva no Existe!!")
        return
    posicion = lista_Reserva.index(busqueda_Reserva)
    print("¡¡Reserva Encontrada!!")
    print(f"Posicion: {posicion}")
    print("______________________________")
    print(f"Codigo: {busqueda_Reserva ["Codigo"]}")
    print(f"Nombre: {busqueda_Reserva ["Nombre"]}")
    print(f"Noches: {busqueda_Reserva ["Noches"]}")
    print(f"Valor por Noche: {busqueda_Reserva ["Valor"]}")
    print(f"Total: {busqueda_Reserva ["Total"]}")
    print(f"Categoria: {busqueda_Reserva ["Categoria"]}")
    print("______________________________")
#Opcion 1 Menu
def registrar_Reserva(lista_Reserva):
    solicitar_Codigo = str(input("Ingrese codigo: ")).strip()
    if validar_Codigo (solicitar_Codigo):
        print("El codigo no puede estar vacio!!!")
        return
    solicitar_Nombre = str(input("Ingrese Nombre para Reserva: ")).strip()
    if validar_Nombre (solicitar_Nombre):
        print("El nombre no puede estar vacio!!")
        return
    try:
        solicitar_Noches = int(input("Ingrese cantidad de noches: "))
    except ValueError:
        print("Ingreso invalido!! \n Ingrese solo numeros Enteros")
        return
    if validar_Noches (solicitar_Noches):
        print("El numero debe ser mayor a 0")
        return
    try:
        solicitar_Valor = int(input("Ingrese valor noche: "))
    except ValueError:
        print("Ingreso invalido!! \n Ingrese solo numeros Enteros")
        return
    if validar_Valor (solicitar_Valor):
        print("El numero debe ser mayor a 0")
        return
    #Calcular automaticamente
    total = solicitar_Noches * solicitar_Valor
    categoria = calcular_Categoria (total)
    reserva_Cliente = {"Codigo": solicitar_Codigo, "Nombre": solicitar_Nombre, "Noches": solicitar_Noches, "Valor": solicitar_Valor,  "Total": total, "Categoria": categoria}
    lista_Reserva.append(reserva_Cliente)
    print("¡¡¡Reserva Exitosa!!!")
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