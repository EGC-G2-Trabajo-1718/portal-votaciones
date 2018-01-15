# coding=utf-8
import json
import urllib3
from datetime import datetime
from time import strptime


def extraccion_datos(uri):
    http = urllib3.PoolManager()
    r = http.request('GET', uri)
    datos = json.loads(r.data.decode('utf-8'))

    return datos



def parseEdades():
    edades = ["18-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90+"]
    array_recuento = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    datos = extraccion_datos('http://localhost:3000/edades');

    def acumulador(recuento):

        if (edad_objeto >= 18 and edad_objeto <= 20):
            recuento[0] = recuento[0] + 1
        elif (edad_objeto >= 21 and edad_objeto <= 30):
            recuento[1] = recuento[1] + 1
        elif (edad_objeto >= 31 and edad_objeto <= 40):
            recuento[2] = recuento[2] + 1
        elif (edad_objeto >= 41 and edad_objeto <= 50):
            recuento[3] = recuento[3] + 1
        elif (edad_objeto >= 51 and edad_objeto <= 60):
            recuento[4] = recuento[4] + 1
        elif (edad_objeto >= 61 and edad_objeto <= 70):
            recuento[5] = recuento[5] + 1
        elif (edad_objeto >= 71 and edad_objeto <= 80):
            recuento[6] = recuento[6] + 1
        elif (edad_objeto >= 81 and edad_objeto <= 90):
            recuento[7] = recuento[7] + 1
        else:
            recuento[8] = recuento[8] + 1

        return recuento

    for i in datos[0]['data']:
        edad_objeto = i['edad']
        acumulador(array_recuento)

    return edades, array_recuento;


def parseLugaresGeograficos(opcion):
    sitios = []
    array_recuento = []

    if (opcion == "ciudades"):
        datos = extraccion_datos('http://localhost:3000/ciudades');
    elif (opcion == "pronvicias"):
        datos = extraccion_datos('http://localhost:3000/provincias');
    elif (opcion == "comunidades"):
        datos = extraccion_datos('http://localhost:3000/comunidades');
    elif (opcion == "paises"):
        datos = extraccion_datos('http://localhost:3000/paises');

    for i in datos[0]['data']:
        for key in i.keys():
            sitios.append(key.encode('utf-8'))
            array_recuento.append(i[key])

    return sitios, array_recuento



def obtener_censo(id,auth):
    if((id and auth) != None):
        datos = extraccion_datos('http://egc-recuento1718.es/api/polls/' + str(id) + '/' + str(auth));
    else:
        datos = extraccion_datos('http://localhost:3000/recuentoDatosCompletos');
    return datos[0]['total_voters']


def obtener_votantes(id,auth):
    if ((id and auth) != None):
        datos = extraccion_datos('http://egc-recuento1718.es/api/polls/' + str(id) + '/' + str(auth));
    else:
        datos = extraccion_datos('http://localhost:3000/recuentoDatosCompletos');
    return datos[0]['total_votes']


def votosPorOpcionNuevaApi(id,auth):
    opciones = []
    votos = []

    if ((id and auth) != None):
        datos = extraccion_datos('http://egc-recuento1718.es/api/vote/' + str(id) + '/' + str(auth));
    else:
        datos = extraccion_datos('http://localhost:3000/recuentoResultados');

    i = 0
    for valor in datos[0]:
        if(i==0):
            opciones.append(valor.encode('utf-8'))
        elif(i%2 == 0):
            opciones.append(valor.encode('utf-8'))
        elif(i%2 !=0):
            votos.append(valor)

        i = i+1

    return opciones, votos



def votosPorTramoHorario():
    tramos = ["00:00 - 05:00", "05:00 - 10:00", "10:00 - 15:00", "15:00 - 20:00", "20:00 - 24:00"]
    array_recuento = [0, 0, 0, 0, 0]

    def recuento(recuento):
        if (hora_formato >= inicio_primerTramo and hora_formato <= fin_primerTramo):
            array_recuento[0] = array_recuento[0] + 1
        elif (hora_formato >= inicio_segundoTramo and hora_formato <= fin_segundoTramo):
            array_recuento[1] = array_recuento[1] + 1
        elif (hora_formato >= inicio_tercerTramo and hora_formato <= fin_tercerTramo):
            array_recuento[2] = array_recuento[2] + 1
        elif (hora_formato >= inicio_cuartoTramo and hora_formato <= fin_cuartoTramo):
            array_recuento[3] = array_recuento[3] + 1
        elif (hora_formato >= inicio_quintoTramo and hora_formato <= fin_quintoTramo):
            array_recuento[4] = array_recuento[4] + 1

    inicio_primerTramo = datetime(*strptime("00:00:00", "%H:%M:%S")[0:6]).time()
    fin_primerTramo = datetime(*strptime("05:00:00", "%H:%M:%S")[0:6]).time()
    inicio_segundoTramo = datetime(*strptime("05:00:01", "%H:%M:%S")[0:6]).time()
    fin_segundoTramo = datetime(*strptime("10:00:00", "%H:%M:%S")[0:6]).time()
    inicio_tercerTramo = datetime(*strptime("10:00:01", "%H:%M:%S")[0:6]).time()
    fin_tercerTramo = datetime(*strptime("15:00:00", "%H:%M:%S")[0:6]).time()
    inicio_cuartoTramo = datetime(*strptime("15:00:01", "%H:%M:%S")[0:6]).time()
    fin_cuartoTramo = datetime(*strptime("20:00:00", "%H:%M:%S")[0:6]).time()
    inicio_quintoTramo = datetime(*strptime("20:00:01", "%H:%M:%S")[0:6]).time()
    fin_quintoTramo = datetime(*strptime("23:59:59", "%H:%M:%S")[0:6]).time()

    datos = extraccion_datos('http://localhost:3000/horas')

    for i in datos[0]['data']:
        hora = i['momento'].split(' ')[1]
        hora_formato = datetime(*strptime(hora, "%H:%M:%S")[0:6]).time()
        recuento(array_recuento)


    return tramos,array_recuento

def parseEdades2():
    edades = ["20-25", "25-30", "30-35", "35-40", "40-45", "45-50"]
    array_recuento = [0, 0, 0, 0, 0, 0]

    datos = extraccion_datos('http://localhost:3000/edades');

    def acumulador(recuento):

        if (edad_objeto >= 20 and edad_objeto <= 25):
            recuento[0] = recuento[0] + 1
        elif (edad_objeto >= 25 and edad_objeto <= 30):
            recuento[1] = recuento[1] + 1
        elif (edad_objeto >= 30 and edad_objeto <= 35):
            recuento[2] = recuento[2] + 1
        elif (edad_objeto >= 35 and edad_objeto <= 40):
            recuento[3] = recuento[3] + 1
        elif (edad_objeto >= 40 and edad_objeto <= 45):
            recuento[4] = recuento[4] + 1

        else:
            recuento[5] = recuento[5] + 1

        return recuento

    for i in datos[0]['data']:
        edad_objeto = i['edad']
        acumulador(array_recuento)

    return edades, array_recuento;

print parseEdades2()


