import time
import csv
csv.field_size_limit(2147483647)
from DataStructures.List import array_list as lt


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {"viajes": None}
    catalog["viajes"] = lt.new_list()
    return catalog


# Funciones para la carga de datos
def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    id = 0    
    start = get_time()
    taxis = filename
    input_file = csv.DictReader(open(taxis, encoding='utf-8'))
    
    for viaje in input_file:
        viaje["id"]=id #El dictreader me da cada fila como un dict, 
                       #pongo una llave id para que sea fácil identificar cada viaje
        viaje["passenger_count"] = int(viaje["passenger_count"])
        viaje["trip_distance"] = float(viaje["trip_distance"])
        viaje["pickup_longitude"] = float(viaje["pickup_longitude"])
        viaje["pickup_latitude"] = float(viaje["pickup_latitude"])
        viaje["rate_code"] = int(viaje["rate_code"])
        viaje["dropoff_longitude"] = float(viaje["dropoff_longitude"])
        viaje["dropoff_latitude"] = float(viaje["dropoff_latitude"])
        viaje["fare_amount"] = float(viaje["fare_amount"])
        viaje["extra"] = float(viaje["extra"])
        viaje["mta_tax"] = float(viaje["mta_tax"])
        viaje["tip_amount"] = float(viaje["tip_amount"])
        viaje["tolls_amount"] = float(viaje["tolls_amount"])
        viaje["improvement_surcharge"] = float(viaje["improvement_surcharge"])
        viaje["total_amount"] = float(viaje["total_amount"])

        lt.add_last(catalog["viajes"], viaje)   
        id += 1
    end = get_time()
    tiempo = delta_time(start, end)
    
    total = lt.size(catalog["viajes"])
    menor = 1000000000
    mayor = 0.0
    for i in range(0, total):
        viaje = lt.get_element(catalog["viajes"], i)
            #calcula el viaje con menor distancia y el mayor
        if viaje["trip_distance"] < menor and viaje["trip_distance"] > 0.0:
            menorid = viaje["id"]
            menor = viaje["trip_distance"]
            fecha_menor = viaje["pickup_datetime"]
            costo_menor = viaje["total_amount"]
            
        if viaje["trip_distance"] > mayor:
            mayorid = viaje["id"]
            mayor = viaje["trip_distance"]
            fecha_mayor = viaje["pickup_datetime"]
            costo_mayor = viaje["total_amount"]
    
    primeros = []
    for i in range (0,5):
        viaje = lt.get_element(catalog["viajes"], i)
        fech_ini= str(viaje["pickup_datetime"])
        fech_fin= str(viaje["dropoff_datetime"])
        hor_ini= fech_ini[11:]
        x_ini= hor_ini.split(":")
        Dura_ini= int(x_ini[0])*60 + int(x_ini[1])
        hor_fin= fech_fin[11:]
        x_fin= hor_fin.split(":")
        Dura_fin= int(x_fin[0])*60 + int(x_fin[1])
        if Dura_fin >= Dura_ini:  
            Dura= Dura_fin - Dura_ini
        else:  
            # asumimos que solo pasa al día siguiente
            Dura= (1440 - Dura_ini) + Dura_fin
        info = {
            "Id_trayecto": viaje["id"],
            "Fecha/Hora inicio": viaje["pickup_datetime"],
            "Fecha/Hora destino": viaje["dropoff_datetime"],
            "Duración en (m)": Dura,
            "Distancia": viaje["trip_distance"],
            "Costo_total": viaje["total_amount"]}
        primeros.append(info)
    
    ultimos = []
    for i in range (total-5, total):
        viaje = lt.get_element(catalog["viajes"], i)
        fech_ini= str(viaje["pickup_datetime"])
        fech_fin= str(viaje["dropoff_datetime"])
        hor_ini= fech_ini[11:]
        x_ini= hor_ini.split(":")
        Dura_ini= int(x_ini[0])*60 + int(x_ini[1])
        hor_fin= fech_fin[11:]
        x_fin= hor_fin.split(":")
        Dura_fin= int(x_fin[0])*60 + int(x_fin[1])
        if Dura_fin >= Dura_ini:  
            Dura= Dura_fin - Dura_ini
        else:  
            # asumimos que solo pasa al día siguiente
            Dura= (1440 - Dura_ini) + Dura_fin
        viaje = lt.get_element(catalog["viajes"], i)
        info = {
            "Id_trayecto": viaje["id"],
            "Fecha/Hora inicio": viaje["pickup_datetime"],
            "Fecha/Hora destino": viaje["dropoff_datetime"],
            "Duración en (min)": Dura,
            "Distancia": viaje["trip_distance"],
            "Costo_total": viaje["total_amount"]}
        ultimos.append(info)
        
    return tiempo, total, menorid, fecha_menor, costo_menor, mayorid, fecha_mayor, costo_mayor, primeros, ultimos


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    tam = lt.size(catalog["viajes"])
    if id >= 0 and id < tam:
        for i in range(0,tam):
            dato = lt.get_element(catalog["viajes"], i)
            if id == dato["id"]:
                return dato
    else:
        return None


def req_1(catalog, pasajeros):
    """
    Retorna el resultado del requerimiento 1 - Juliana Rodríguez
    Calcular la información promedio de los trayectos dado una 
    cantidad de pasajeros.
    """
    # TODO: Modificar el requerimiento 1
    start = get_time()
    trayectos = 0
    duracion = 0 
    costo_total = 0
    distancia = 0
    peajes = 0
    propina = 0
    tipo_pago = {"CREDIT_CARD": 0, "CASH": 0, "NO_CHARGE": 0, "UNKNOWN": 0}
    fechas = []
    frecuencias_fechas = []
    
    tam = lt.size(catalog)
    for i in range(0,tam):
        viaje = lt.get_element(catalog["viajes"],i)
        fech_ini= str(viaje["pickup_datetime"])
        fech_fin= str(viaje["dropoff_datetime"])
        hor_ini= fech_ini[11:]
        x_ini= hor_ini.split(":")
        Dura_ini= int(x_ini[0])*60 + int(x_ini[1])
        hor_fin= fech_fin[11:]
        x_fin= hor_fin.split(":")
        Dura_fin= int(x_fin[0])*60 + int(x_fin[1])
        Dura= Dura_fin - Dura_ini
        
        if viaje["passenger_count"] == int(pasajeros):
            trayectos += 1
            duracion += Dura
            costo_total += viaje["total_amount"]
            distancia += viaje["trip_distance"]
            peajes += viaje["tolls_amount"]
            propina += viaje["tip_amount"]
            
            if viaje["payment_type"] == "CREDIT_CARD":
                tipo_pago["CREDIT_CARD"]+=1          
            elif viaje["payment_type"] == "CASH":
                tipo_pago["CASH"]+=1
            elif viaje["payment_type"] == "NO_CHARGE":
                tipo_pago["NO_CHARGE"]+=1
            elif viaje["payment_type"] == "UNKNOWN":
                tipo_pago["UNKNOWN"]+=1
                
            fecha_i = str(viaje["pickup_datetime"])[:10]
            if fecha_i not in fechas:
                fechas.append(fecha_i)
                frecuencias_fechas.append(1)
            else:
                ind = fechas.index(fecha_i)
                frecuencias_fechas[ind] += 1

    duracion_prom = duracion/trayectos
    costo_prom = costo_total/trayectos
    distancia_prom = distancia/trayectos
    peajes_prom = peajes/trayectos
    propina_prom = propina/trayectos
    
    # encontrar el pago más frecuente
    pago_mayor = "CREDIT_CARD"
    mayor = tipo_pago["CREDIT_CARD"]
    if tipo_pago["CASH"] > mayor:
        mayor = tipo_pago["CASH"]
        pago_mayor = "CASH"
    elif  tipo_pago["NO_CHARGE"]>mayor:
        mayor = tipo_pago["NO_CHARGE"]
        pago_mayor = "NO_CHARGE"
    elif tipo_pago["UNKNOWN"]>mayor:
        mayor = tipo_pago["UNKNOWN"]
        pago_mayor = "UNKNOWN"
    
    pago_mas_usado = pago_mayor + str(mayor)
    
    # Encontrar el día más frecuente
    fracuencia = max(frecuencias_fechas)
    f = frecuencias_fechas.index(fracuencia)
    fecha_repetida = fechas[f]
    
    end = get_time()  
    tiempo = delta_time(start, end)
    return tiempo, trayectos, duracion_prom, costo_prom, distancia_prom, peajes_prom, pago_mas_usado, propina_prom, fecha_repetida


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
