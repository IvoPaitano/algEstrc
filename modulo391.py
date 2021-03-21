#e391
#Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

#e391a
#Parametros de entrada : 3, Horas - Minutos - Segundos (h, m, s)
#Valores de salida : 1, duracion en segundos (ds)
#Definiremos una funcion e391a que que recibira 3 parametros(h, m, s)
#Dentro del cuerpo haremos calcularemos la duracion en segundos(ds) la retornamos
# ds = h*3600 + m*60 + s*1
#Damos por hecho que se ingresara el valor de horas, minutos y segundos por separado y NO en formato(hh:mm:ss)

def e391a(h, m, s):
    ds = h*3600 + m*60 + s*1
    return ds

#e391b
#Parametros de entrada : 1, Cantidad de segundos(cs)
#Valores de salida : 3, Horas - Minutos - Segundos(h, m, s)
#Definiremos una funcion e391b que recibira un parametro(cs)
#Dentro del cuerpo calcularemos las horas minutos y segundos con ayuda de la division entera.
#h = cs % 3600
#m = (cs % 3600) // 60
#s = (cs % 3600) % 60

def e391b(cs):
    h = cs // 3600
    m = (cs % 3600) // 60
    s = (cs % 3600) % 60
    return h, m, s



