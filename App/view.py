import sys
import tabulate as tb
import App.logic as logic

default_limit = 1000
sys.setrecursionlimit(default_limit*10) 

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control    

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = input('Diga el archivo que quiere evaluar (small, medium, large)\n')
    filename = "data/taxis-"+filename+".csv"
    tiempo, total, menorid, fecha_menor, costo_menor, mayorid, fecha_mayor, costo_mayor, primeros, ultimos = logic.load_data(control, filename)
    print("\nTiempo de carga: "+str(tiempo)+" [ms].\
        \nTotal de trayectos: "+str(total)+" trayectos.\
        \nEl trayecto con menor distancia es el "+str(menorid)+":  \t Fecha: "+str(fecha_menor)+"\tCosto: "+str(costo_menor)+"\n\
        \nEl trayecto con mayor distancia es el "+str(mayorid)+":  \t Fecha: "+str(fecha_mayor)+"\tCosto: "+str(costo_mayor)+"\n\
        \nLos primeros 5 viajes fueron:\n"+ tb.tabulate(primeros, headers="keys") +"\n\nLos últimos 5 viajes fueron: \n"+ tb.tabulate(ultimos, headers="keys")+"\n")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    identificacion = int(input("Indique el Id del viaje que desea ver: "))
    dato = logic.get_data(control, identificacion)
    print(dato)

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pas = input("Indique la cantidad de pasajeros: ")
    tiempo, trayectos, duracion_prom, costo_prom, distancia_prom, peajes_prom, pago_mas_usado, propina_prom, fecha_repetida, frecuencia = logic.req_1(control, pas)
    print("\nTiempo de ejecución: "+str(tiempo)+" [ms].\
        \nCantidad de trayectos con "+str(pas)+" pasajeros: "+str(trayectos)+"\
        \nEstadísitcas:\n\t- Duración promedio [min] de los trayectos: "+str(duracion_prom)+"\
        \n\t- Costo promedio [dólares] de los trayectos: "+str(costo_prom)+"\
        \n\t- Distancia promedio [millas] de los trayectos: "+str(distancia_prom)+"\
        \n\t- Promedio costos de peajes: "+str(peajes_prom)+"\
        \n\t- Tipo de pago más usado: "+str(pago_mas_usado)+"\
        \n\t- Pago propina promedio de los trayectos: "+str(propina_prom)+"\
        \n\t- La fecha con más trayectos es "+fecha_repetida+" donde hubo "+str(frecuencia)+" trayectos.")

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    pago = input("Indique el tipo de pago que desea consultar (CREDIT_CARD, CASH, NO_CHARGE, UNKNOWN): ")
    tiempo, contador, duracion, costo, distancia_total, peajes_total, cantidad_pasa, propina, fecha_mayor = logic.req_2(control, pago)

    data = [
        ["Tiempo de consulta [ms]", str(tiempo)],
        ["Total de trayectos con tipo de pago " + str(pago), str(contador)],
        ["Duración promedio de los viajes [min]", str(duracion)],
        ["Costo promedio de los viajes [USD]", str(costo)],
        ["Distancia promedio de los viajes [millas]", str(distancia_total)],
        ["Peajes promedio de los viajes [USD]", str(peajes_total)],
        ["Cantidad de pasajeros más frecuente “#número de pasajeros – cantidad”", str(cantidad_pasa)],
        ["Propina promedio [USD]", str(propina)],
        ["Fecha de finalización de trayecto con mayor frecuencia ", str(fecha_mayor)]
    ]

    print("\n=== Resultados del Requerimiento 2 ===")
    print(tb.tabulate(data, headers=["Descripción", "Valor"]))
    print("=======================================\n")

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    menor= input("Indique el valor menor del precio total pagado: ")
    mayor= input("Indique el valor mayor del precio total pagado: ")
    tiempo, contador, duracion, costo, distancia_total, peajes_total, cantidad_pasa, propina, fecha_mayor = logic.req_3(control, mayor, menor)  
    print("\nTiempo de ejecución: "+str(tiempo)+" [ms].\
        \nCantidad de trayectos con precio total pagado entre "+str(menor)+" y "+str(mayor)+": "+str(contador)+"\
        \nEstadísitcas:\n\t- Duración promedio [min] de los trayectos: "+str(duracion)+"\
        \n\t- Costo promedio [dólares] de los trayectos: "+str(costo)+"\
        \n\t- Distancia promedio [millas] de los trayectos: "+str(distancia_total)+"\
        \n\t- Promedio costos de peajes: "+str(peajes_total)+"\
        \n\t- Cantidad de pasajeros más frecuente “#número de pasajeros – cantidad”: "+str(cantidad_pasa)+"\
        \n\t- Pago propina promedio de los trayectos: "+str(propina)+"\
        \n\t- La fecha con más trayectos es "+fecha_mayor+".")
    return None


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("\n=== Requerimiento 4: Combinación de barrios con mayor/menor costo promedio ===")

    filtro = input("Digite filtro (MAYOR/MENOR): ").strip().upper()
    fecha_ini = input("Digite fecha inicial (YYYY-MM-DD): ").strip()
    fecha_fin = input("Digite fecha final (YYYY-MM-DD): ").strip()

    resultado = logic.req4(control, filtro, fecha_ini, fecha_fin)

    if "mensaje" in resultado:
        print("\n", resultado["mensaje"])
    else:
        print(f"\nFiltro aplicado: {resultado['filtro']}")
        print(f"Total de trayectos analizados: {resultado['total_trayectos']}")
        print(f"Barrio origen: {resultado['barrio_origen']}")
        print(f"Barrio destino: {resultado['barrio_destino']}")
        print(f"Distancia promedio: {resultado['distancia_promedio']:.2f} millas")
        print(f"Duración promedio: {resultado['duracion_promedio']:.2f} minutos")
        print(f"Costo promedio: ${resultado['costo_promedio']:.2f}")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    return None


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    return None



# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
