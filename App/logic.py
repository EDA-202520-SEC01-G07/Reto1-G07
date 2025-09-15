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
    
    tam = lt.size(catalog["viajes"])
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
        if Dura_fin >= Dura_ini:  
            Dura= Dura_fin - Dura_ini
        else:  
            # asumimos que solo pasa al día siguiente
            Dura= (1440 - Dura_ini) + Dura_fin
        
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
    
    pago_mas_usado = pago_mayor +" - "+str(mayor)
    
    # Encontrar el día más frecuente
    frecuencia = max(frecuencias_fechas)
    f = frecuencias_fechas.index(frecuencia)
    fecha_repetida = fechas[f]
    
    end = get_time()  
    tiempo = delta_time(start, end)
    return tiempo, trayectos, duracion_prom, costo_prom, distancia_prom, peajes_prom, pago_mas_usado, propina_prom, fecha_repetida, frecuencia


def req_2(catalog, pago):
    start = get_time()
    total = lt.size(catalog["viajes"])
    contador = 0
    Duracion = 0
    filtro = []
    costo_total = 0
    distancia_total = 0
    peajes_total = 0
    pasajeros = {}
    pasa = 0
    cantidad = 0
    propina = 0
    fecha = {}
    fech = 0
    
    for i in range(0, total):
        viaje = lt.get_element(catalog["viajes"], i)
        if viaje["payment_type"] == pago:
            contador += 1
            filtro.append(viaje)
    
    for viaje in filtro:
        fech_ini = str(viaje["pickup_datetime"])
        fech_fin = str(viaje["dropoff_datetime"])

        hor_ini = fech_ini[11:]
        x_ini = hor_ini.split(":")
        Dura_ini = int(x_ini[0]) * 60 + int(x_ini[1])

        hor_fin = fech_fin[11:]
        x_fin = hor_fin.split(":")
        Dura_fin = int(x_fin[0]) * 60 + int(x_fin[1])

        if Dura_fin >= Dura_ini:
            Dura = Dura_fin - Dura_ini
        else:
            Dura = (1440 - Dura_ini) + Dura_fin

        Duracion += Dura
        costo_total += viaje["total_amount"]
        distancia_total += viaje["trip_distance"]
        peajes_total += viaje["tolls_amount"]
        propina += viaje["tip_amount"]

        if viaje["passenger_count"] in pasajeros:
            pasajeros[viaje["passenger_count"]] += 1
        else:
            pasajeros[viaje["passenger_count"]] = 1

        fecha_fin = viaje["dropoff_datetime"][:10]
        if fecha_fin in fecha:
            fecha[fecha_fin] += 1
        else:
            fecha[fecha_fin] = 1
    
    for key in pasajeros:
        if pasajeros[key] > pasa:
            pasa = pasajeros[key]
            cantidad = key
    
    fecha_mas_frec = None
    for key in fecha:
        if fecha[key] > fech:
            fech = fecha[key]
            fecha_mas_frec = key
    
    duracion = Duracion / contador
    costo = costo_total / contador
    distancia_total = distancia_total / contador
    peajes_total = peajes_total / contador
    propina = propina / contador
    cantidad_pasa = str(cantidad) + "-" + str(pasa)
    
    end = get_time()
    tiempo = delta_time(start, end)
    
    return round(tiempo,2), contador, round(duracion,2), round(costo,2), round(distancia_total,2), round(peajes_total,2), cantidad_pasa, round(propina,4), fecha_mas_frec


def req_3(catalog, maximo, minimo):
    start=get_time()
    tamano=lt.size(catalog["viajes"])
    trayectos=0
    duracion=0
    costo=0
    distancia=0
    peajes=0
    propina=0
    frecuencias_pasa={}
    frecuencias_fechas={}
    
    for i in range(0,tamano):
        viaje=lt.get_element(catalog["viajes"],i)
        if viaje["total_amount"]>=minimo and viaje["total_amount"]<=maximo:
            trayectos+=1
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
                Dura= (1440 - Dura_ini) + Dura_fin
                
            duracion+=Dura
            costo+=viaje["total_amount"]
            distancia+=viaje["trip_distance"]
            peajes+=viaje["tolls_amount"]
            propina+=viaje["tip_amount"]
            
              
            if viaje["passenger_count"] in frecuencias_pasa:
                frecuencias_pasa[viaje["passenger_count"]]+=1
            else:
                frecuencias_pasa[viaje["passenger_count"]]=1
            
            if fech_fin in frecuencias_fechas:
                frecuencias_fechas[fech_fin]+=1
            else:
                frecuencias_fechas[fech_fin]=1
            
    duracion_prom=duracion/trayectos
    costo_prom=costo/trayectos
    distancia_prom=distancia/trayectos
    peajes_prom=peajes/trayectos
    propina_prom=propina/trayectos
       
    max_cantidad = 0
    num_pasajeros = 0
    for key in frecuencias_pasa:
        if frecuencias_pasa[key] > max_cantidad:
            max_cantidad = frecuencias_pasa[key]  
            num_pasajeros = key              

    max_cpasajeros = str(num_pasajeros) + " - " + str(max_cantidad)

    max_fech = 0
    fecha_frec = None
    for key in frecuencias_fechas:
        if frecuencias_fechas[key] > max_fech:
            max_fech = frecuencias_fechas[key]
            fecha_frec = key             
        
    end=get_time()
    tiempo=delta_time(start,end)
        
    return round(tiempo,2), trayectos, round(duracion_prom,2), round(costo_prom,2), round(distancia_prom,2), round(peajes_prom,2), max_cpasajeros, round(propina_prom,4), fecha_frec
              
#Función auxiliar apara cargar datos del nyc-neighborhoods.csv
def load_data_neigh()            
    barrios = lt.new_list()
    input_file = csv.DictReader(open("data/nyc-neighborhoods.csv", encoding='utf-8'))
    for barrio in input_file:
        lt.add_last(barrios, barrio)   
    return barrios

def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog,costo_tipo, fecha_inicial, fecha_final):
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
