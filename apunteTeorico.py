#Ejercicios 1.x
def cuadrado(n):
    return n * n

def suma_cuadrado_nan(n1, n2):
    suma = 0
    for x in range(n1, n2+1):
        suma = suma + cuadrado(x)
    return suma

#Funcion 'Cuadrados'
def problema192(n1,n2):
    mensajeBienvenida = 'Bienvenido al programa.'
    mensajeDespedida = 'Es todo por hoy, hasta luego.'

    print(mensajeBienvenida)
    # n1 = int(input('Introduzca n1:'))
    # n2 = int(input('Introduzca n2:'))
    for x in range(n1, n2+1):
        print(x,':',x * x)
    print(mensajeDespedida)

def producto():
    n1 = int(input('Ingrese n1:'))
    n2 = int(input('Ingrese n2:'))
    return n1*n2


def facto(n):
    sum = 1
    for x in range(sum, n+1):
        sum = sum * x
    return(sum)

def operaciones(n1, n2):
    print('Suma:',n1+n2,'\nResta:',n1-n2,'\nDivision:',n1/n2,'\nMultiplicacion:',n1*n2)

def tabla(n):
    for x in range(1, 11):
        print(n,'*',x,': =',n*x)

def milengua(palabra):
    for x in range(1000):
        print(palabra ,end=' ')


#Ejercicios 2.x

def ametrico():
    print('Convierte medidas inglesas a sistema metrico.')

    millas = int(input('Cuantas millas?: '))
    pies = int(input('Cuentos pies?: '))
    pulgadas = int(input('Cuantas pulgadas?: '))

    metros = 1609.334 * millas + 0.3048 * pies + 0.0254 * pulgadas
    print('La longitud es de : ', metros, 'metros.')

def reglasAs(a, b, c):
    ea = ((b * b) - (4 * a * c)) / (2 * a)
    eb = ((b * b) - (4 * a * c)) // (2 * a)
    ec = (b * b - 4 * a * c) / (2 * a)
    ed = b * b - 4 * a * c / 2 * a
    ee = (b * b) - (4 * a * c / 2 * a)
    ef = 1 / 2 * b
    eg = b / 2

    print('ea: '+str(ea),'eb: '+str(eb),'ec: '+str(ec),'ed: '+str(ed),'ee: '+str(ee),'ef: '+str(ef),'eg: '+str(eg), sep='\n')

def reglasAsf(a, b, c):
    ea = ((b * b) - (4 * a * c)) / (2 * a)
    eb = ((b * b) - (4 * a * c)) // (2 * a)
    ec = (b * b - 4 * a * c) / (2 * a)
    ed = b * b - 4 * a * c / 2 * a
    ee = (b * b) - (4 * a * c / 2 * a)
    ef = 1 / 2 * b
    eg = b / 2

    print('ea: '+str(ea),'eb: '+str(eb),'ec: '+str(ec),'ed: '+str(ed),'ee: '+str(ee),'ef: '+str(ef),'eg: '+str(eg), sep='\n')

list(range(10,20))

#2.6.1 a
#Escribir un ciclo definidio para imprimir por pantalla todos los numeros entre 10 y 20.
#Valores de entrada : -
#Valores de salida : print n
#Diseño :
# Crear un ciclo definidio(10,20)
# en el cuerpo imprimir el nombre.

def a261():
    for x in range(11,20):
        print(x)

#261b
#Escribir un ciclo definido que salude por pantalla a sus cinco mejores amigos/as.
#Damos por sentado que el saludo es personal y no grupal.
#Al saber los nombres no necesitamos parametros.
#Parametros de entrada : -
#Valores de salida : print hola + nombre
# Crear una lista con los 5 nombres.
# Crear un ciclo definido con la lista como expresion(secuencia de valores)
# dentro del ciclo imprimir un saludo + el nombre.

def b261():
    amigos = ('Ivo', 'Ezequiel', 'Diego', 'Nico', 'Monty')
    for nombre in amigos:
        print('Hola',nombre)
#261c
#Escribir un programa que use un ciclo definido con rango numérico, que pregunte los 
#nombres de sus cinco mejores amigos/as, y los salude.
#Damos por sentado que el programa primero pide TODOS los nombres y luego saluda a cada uno.
#Se aclara que el rango es de 5
#Valores de entrada : 5, pediremos TODOS los nombres uno por uno apoyandonos en input y guardandolos en una var.
#Valores de salida : imprimiremos el saludo a CADA amigo con su respectivo nombre.

#Crearemos una lista vacia llamada amigos.
#Crear un ciclo definidio con rango 6
#En el cuerpo del ciclo pediremos los nombres y los guardaremos en una variable amigoN
#por cada iteracion se agregara el nombre del amigo a la lista 'amigos'
#Crearemos otro ciclo definido con la lista amigos como expresion
#Dentro del cuerpo imprimiremos un saludo por cada amigo con su respectivo nombre.

def c261():
    amigos = []
    for x in range(1,6):
        amigon = input('Nombre amigo '+str(x)+':')
        amigos.append(amigon)
    for nombre in amigos:
        print('Hola '+nombre)


#261d
#Escribir un programa que use un ciclo definido con rango numérico, que pregunte los 
#nombres de sus seis mejores amigos/as, y los salude.
#El problema anterior puede solucionar este mismo con solo cambiar el rango al pedir los nombres de los amigos.

def c261():
    amigos = []
    for x in range(1,7):
        amigon = input('Nombre amigo '+str(x)+':')
        amigos.append(amigon)
    for nombre in amigos:
        print('Hola '+nombre)

#261e
#Escribir un programa que use un ciclo definido con rango numérico, que averigue a
#cuántos amigos quieren saludar, les pregunte los nombres de esos amigos/as, y los salude.

#Podemos apoyarnos en la solucion del ejercicio 261c modificarlo y crear la solucion
#Pedir la cantidad de amigos a saludar y guardarla en una var.
#Modificamos la funcion de 261c y le pedimos un parametro este sera la cantidad de amigos a saludar
#modificamos el primer ciclo y cambiamos el segundo valor de range por el parametro pedido + (namigos+1)
#llamamos a la funcion.

def c261m(namigos):
    amigos = []
    for x in range(1,namigos+1):
        amigon = input('Nombre amigo '+str(x)+':')
        amigos.append(amigon)
    for nombre in amigos:
        print('Hola '+nombre)

def e261():
    namigos = int(input('Ingrese cantidad de amigos.'))
    c261m(namigos)

#262
#Parametros de entrada : cantidad de pesos(C), tasa de interes (x) y numero de años (n)
#Salida : monto final a obtener.
#Formula = Cn = Cx(1+x/100)^n

def e262(C, x, n):
    cn = C * ((1 + x/100)**n)
    return cn

#263
#Apoyandonos en la funcion anterior debemos pedir al usuario cada uno de los parametros que pide la funcion.
#Para eso ademas de pedirlos debemos transormarlos a float o int segun lo necesito la funcion

def e263():
    c = float(input('Cantidad de pesos inicial: '))
    x = float(input('Tasa de interes: '))
    n = float(input('Numero de años: '))
    print(e262(c, x, n))

#264
#Parametros de entrada : NGradosFahrenheit
#Valor de salida : parametro convertido a grados Celsius
#Formula: F = (9/5)c + 32

def e264(f):
    c = (5/9)*(f-32)
    return c

#265
#Escribir un programa que utilice la función anterior para generar una tabla de
#conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.
#Parametros de entrada : -
#Parametros de salida : imprimir de 10 en 10 de 0 hasta 120F y su equivalente a celsius
#Para que sea de 10 en 10 vamos a definir una variable auxilar que por cada repeticion subira 10F
#y llamaremos a la funcion e264
#Crear un ciclo definido con 12 repeticiones y por cada ciclo se imprimira el valor en F y C  ? F --> C

def e265():
    gf = 0
    for x in range(13):
        print(str(gf)+' F --> C '+str(e264(gf)))
        gf+=10

#266
#266a
#Escribir una función que dado un número entero devuelva 1 si el mismo es impar y 0 si fuera par.
#Valores de entrada : numoer(n)
#Valores de salida : impar(1), o par(0)
#Vamos a apoyarnos en la division entera %2, esto devolvera 1 si es impar y 0 si es par.

def e266a(n):
    return n%2

#e266b 
#Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si fuera par.
#Es igual que la funcion anterior pero con los resultados invertidos
#Para invertir los resultados comprobaremos el valor de retorno, si es 1 devolvemos 0 y si es 0 devolvemos 1

def e266b(n):
    if n%2 == 0:
        return 1
    else:
        return 0

#e266c
#Escribir una función que dado un número entero devuelva el dígito de las unidades. Por ejemplo, para 153 debe devolver 3.
#Parametros : numero(n)
#Valores de salida : cantidad de digitos(nd)
#Para saber la cantidad de digitos vamos a apoyarnos en la funcion len que viene en python
#pero antes debemos convertir el numero en string para que funcione len, usaremos str

def e266c(n):
    return len(str(n))

#e266d
#Escribir una función que dado un número devuelva el primer número múltiplo de 10 inferior a él. Por ejemplo, para 153 debe devolver 150.
#Parametros de entrada : numero(n)
#Valores de salida : primer multiplo de 10 inferior a n(pmi)
#Primero hay que descartar las opciones en las que no se puede devolver un resultado que no sea error.
#definimos pmi como una variable que sera el valor de retorno.
#Por norma mundial 0 es multiplo de todos los numeros. Si n es 0 retornamos 0
#Si n es menor o igual a 10 retornamos 'no hay multiplo menor', por mas que sea si exista un multiplo este seria 10 y 10 no es menor que 10.
#Por ultimo nos apoyaremos nuevamente en la division absoluta pero por 10(n%10) esto nos dara el resto y se lo restaremos a n lo que nos dara el pmi.
#pmi = n-(n%10)
#recordemos que el pmi debe ser INFERIOR por lo que en la ultima instancia si n es un numero entero, se devolvera el mismo numero entero por lo que debemos restarle 10.

def e266d(n):
    pmi = 0
    if n == 0:
        pmi = 0
    elif n <= 10:
        pmi = 'No existe un multiplo'
    else:
        pmi = n-(n%10)
        if pmi == n:
            pmi = n-10
    return pmi

#e267
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
#Parametros : nInicio(n1), nFin(n2)
#Valores de salida : imprimir todos los numeros pares
#Vamos a tomar los 2 valos y los pondremos como rango en un ciclo definido, indiferentemente de el orden que ponga los numeros
#el programa pondra el menor numero como nInicio y el mayor como nFin, para eso usaremos 2 variables auxiliares
#Luego haremos la comprobacion si un numeor es par(n%2 == 0) y lo imprimimos

def e267(n1, n2):
    ni = 0
    nf = 0
    if n1 < n2:
        ni = n1
        nf = n2
    elif n2 < n1:
        ni = n2
        nf = n1
    else:
        return print(f'No hay numeros entre {n1} y {n2}')
    for n in range(ni, nf):
        if not n%2:
            print(n)
    
#e268
#Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los
#primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen
#mediante la suma de los números naturales desde 1 hasta 𝑛. Es decir, si se piden los primeros 5
#números triangulares, el programa debe imprimir:
#Parametros de entrada : numero(n)
#Valores de salida : imprimir indice -> numero triangular (i -> nn)
#Ejemplo.
#Entrada :5
#Salida : 1 - 1
#         2 - 3
#         3 - 6
#         4 - 10
#         5 - 15
#Formula nn = n(n+1)/2
#CON FORMULA
#Ayudandonos con la formula, crearemos un ciclo definido con rango n
#En el cuerpo del ciclo imprimiremos el indice y el resultado de la formula.

#SIN FORMULA
#Crearemos un ciclo definido con rango n
#Crearemos una variable auxiliar en 0 (sum=0)
#Creamos un ciclo definido con rango i(el indice del ciclo padre)
#En el cuerpo del ciclo usaremos la variable auxiliar sum para ir sumando los valores del indice del ciclo hijo.
#Finalmente imprimiremos el rango del ciclo hijo y la variable auxiliar sum
#y reiniciaremos la variable sum a 0

def e268f(n):
    for i in range(1, n+1):
        nn = int(i*(i+1) / 2)
        print(i, '-', nn) 

def e268(n):
    for i in range(1, n+1):
        sum = 0
        for j in range(1, i+1):
            sum += j
        print(j, '-', sum)

#e269
#Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el
#usuario, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.11.7) e
#imprima el resultado junto con el número de orden correspondiente.
#Ejemplo.
#Damos por hecho que el usuario ingresa una cantidad de valores(cv) y luego procede a ingresar la lista de valores uno por uno hasta llenar cv
#Ejemplo.
#cv = 5
#input : 1 3 2 5 10
#Salida: 1*1 = 1
#        3**2*1 = 6
#        2*1 = 2
#        5*4*3*2*1 = 120
#        10*9*8*7*6*5*4*3*2*1 = 3628800

#Pedimos cantidad de valores(cv)
#Creamos una lista vacia(ln)
#Creamos un ciclo para pedir los valores y los guardamos en una lista
#Pedimos los valores y los guardamos en la lista(ln)
#Creamos un cilo definido con 'rango' lista(ln) - esto recorrera cada uno de los valores de la lista
#Creamos una variable de tipo string vacio(oc)
#creamos un ciclo definido hijo con rango indice del ciclo padre(i)
#al string(oc) le sumamos el indice del ciclo hijo(j) y un signo *, cuando sea el ultimo ciclo solo agregamos el numero.
#Luego fuera del ciclo hijo imprimimos la cadena y el resultado de llamar a la funcion 'fibo'

def e269():
    cv = int(input('Cantidad de valores a ingresar: '))
    ln = []
    for n in range(cv):
        x = int(input(f'Ingrese n[{n}]'))
        ln.append(x)
    for i in ln:
        oc = ''
        for j in range(1, i+1):
            if j == i:
                oc += str(j)    
            else:
                oc += (str(j) + '*')
        print(oc + ' --> ' + str(facto(j)))

#e2610
#Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir.
#Creamos una funcion ficha que recibira 2 parametros (n1,n2) para tener el la plantilla de la ficha.
#el domino tiene un total de 28 fichas con un rango de 0 a 6 y tienen 2 numeros que empiezan desde 0.
#el primer numero aumenta en 1 cuando el segundo numero lo alcanza y el segundo numero vuelve a 0.
#Parametros de entrada : -
#Valores de salida : imprimir todas las fichas
#Crearemos un ciclo definido con rango de 0 a 7
#Dentro crearemos un ciclo hijo con rango 0 a indice del ciclo padre(i)+1
#en el cuerpo del ciclo hijo llamaremos a la funcion ficha y le pasaremos el indice del ciclo padre(i) y el indice del ciclo hijo(j)

def ficha(n1, n2):
    ficha =f'''
     _ _
    |{n1}|{n2}|
     - -
    '''
    return ficha.rstrip()

def e2610():
    for i in range(7):
        for j in range(i+1):
            print(ficha(j,i),end='')
        print('-----------------------------')

#e2611
#Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a 𝑛.
#Vamos a copiar la funcion anterior 2610 y modificarla para resolver este nuevo problema.
#Parametros de entrada : numeroMaximo(nm)
#Parametros de salida : imprimir todas las fichas desde 0 hasta el numeroMaximo(nm)
#Vamos a modificar la funcion para que reciba un parametro numeroMaximo(nm)+1 que reemplazara el valor del rango del ciclo padre.

def e2611(nm):
    for i in range(nm+1):
        for j in range(i+1):
            print(ficha(j,i),end='')
        print('-----------------------------')




#EJERCICIOS 3.X
#e31
#Escribir una función repite_hola que reciba como parámetro un número entero
# n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n.
#Parametros de entrada : n
#Valoes de salida : imprimir hola n veces

def e31(n):
    for i in range(n):
        print('Hola')

#e32/e33
#Escribir otra función repite_hola que reciba como parámetro un número entero n
#y devuelva la cadena formada por n concatenaciones de "Hola". Invocarla con distintos valores
#de n.
#Parametros de entrada : n(int) - saludo(str)
#Valoes de salida : cadena formada n 'saludo'
#Crearemos una variable que contendra la cadena de n 'saludo' (ch)
#Crearemos un ciclo definido con rango(n)
#Dentro del cuerpo por cada iteracion le adherimos 'saludo' a ch
#Al finalizar el ciclo imprimiremos la cadena(ch)

def e32(n, saludo):
    ch = ''
    for i in range(n):
        ch+=saludo
    print(ch)

#e34
#Escribir otra función repite_saludo que reciba como parámetro un número entero
# n y una cadena saludo devuelva el valor de n concatenaciones de saludo. Invocarla con distintos
# valores de n y de saludo.
#No le encontre el sentido a esta funcion por como escribieron el enunciado pero ahi va lo que entendi ¯\_(ツ)_/¯

def e34(n, cadena):
    c = ''
    for i in range(n):
        c+=cadena
    print('concatenaciones de '+cadena+': '+str(n))

#e35Corregir el programa para que:
# Informe el costo en pesos y centavos, en lugar de un número decimal.
# Informe cuál fue el total facturado en la corrida.
# Para pasar el resultado de decimal a pesos y centavos nos apoyaremos en la creacion de una funcion.
# dicha funcion retornara 2 valoes pesos y centavos respectivamente.

def main():
    """El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo."""

    p = float(input("¿Cuánto cuesta 1 segundo de comunicacion?: "))
    n = int(input("¿Cuántas comunicaciones hubo?: "))
    costoTotal = 0
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántos minutos?: "))
        s = int(input("¿Cuántos segundos?: "))
        duracion = a_segundos(h, m, s)
        costo = duracion * p
        pesos, centavos = pyc(costo)
        print("Duracion:", duracion, "segundos. Costo: ",pesos,"Pesos con",centavos,"centavos.")
        costoTotal = costoTotal + costo
    pesosTotal, centavosTotal = pyc(costoTotal)
    print("Costo Total: ",pesosTotal ,"Pesos con",centavosTotal,"centavos.")

def a_segundos(horas, minutos, segundos):
    """Transforma en segundos una medida de tiempo expresada en
    20 horas, minutos y segundos"""
    return 3600 * horas + 60 * minutos + segundos

def pyc(c):
    s = str(c).split('.')
    pesos = s[0]
    centavos = s[1]
    return pesos, centavos


#e392
#Usando las funciones del ejercicio anterior, escribir un programa que pida al
#usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
#por pantalla la duración total en horas, minutos y segundos.

#Parametros de entrada : 6 : Horas minutos y segundos (h, m, s)x2
#Valores de salida : 3, suma de duracion(sd) en horas, minutos, segundos.
#Vamos a llamar la funcion e391a 2 veces para pedir los 2 intervalos.
#Guardaremos el retorno de las 2 veces que llamamos, los sumaremos y llamaremos a la funcion e391b
#para pasar de segundos a h, m, s

from modulo391 import e391a
from modulo391 import e391b
def e392():
    ts = 0
    for x in range(2):
        inh = int(input('Horas :'))
        inm = int(input('Minutos :'))
        ins = int(input('Segundos :'))
        ts += e391a(inh, inm, ins)
    h, m, s = e391b(ts)
    print(f'Total : {h} Horas {m} Minutos {s} Segundos.')

#Ejercicio 3.9.3. Escribir una función que, dados cuatro números, devuelva el mayor producto
#de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
#más grande que se puede obtener entre ellos (8 = −2 × −4).

#Parametros de entrada : 1 Lista(li)
#Valores de salida : 1 - el producto mas grande de 2 de ellos
#Crearemos la funcion e393
#Crearemos una lista vacia(ress)
#Primero crearemos un ciclo con rango lista(li)
#dentro de este ciclo crearemos un ciclo hijo con rango lista(li)
#en cada iteracion a nuestra lista(ress) le agregaremos el producto del indice del ciclo hijo por el indice del ciclo padre
#Finalmente nos apoyaremos en la funcion max para obtener el maximo de una lista(ress)

def e393(li):
    ress = []
    liaux = li.copy()
    for i in li:
        liaux.pop(0)
        for j in liaux:
            n = i * j
            ress.append(n)
    res = max(ress)
    return res

#e394a
#Escribir una función que reciba las coordenadas de un vector en ℝ3 (x,y,z) y devuelva
#la norma del vector, dada por x,y,z = raiz(x°2 + y°2 + z°2)
#Ejemplo: norma(3, 2, -4) → 5.3851

#Parametros de entrada : 3 x, y, z
#Valoes de salida : 1 (norma)

from math import pow
from math import sqrt

def e394a(x, y, z):
    res = sqrt(pow(x,2)+pow(y,2)+pow(z,2))
    return res

#e394b
#Escribir una función que reciba las coordenadas de dos vectores en ℝ3 (x1,y1,z1,x2,y2,z2) 
# y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
#Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)

def e394b(x1, y1, z1, x2, y2, z2):
    xd = x1-x2
    yd = y1-y2
    zd = z1-z2
    return (xd, yd, zd)



#EJERCICIOS 4X
#e41

#El usuario del tarifador nos pide ahora una modificación, ya que no es lo mismo
# la tarifa por segundo de las llamadas cortas que la tarifa por segundo de las llamadas largas.
#Al inicio del programa se informará la duración máxima de una llamada corta, la tarifa de las
# llamadas cortas y la de las largas. Se deberá


def calPrecio(d):
    if d >= 1800:
        p = 0.75
    else:
        p = 0.5
    return p

def main2():
    """El usuario ingresa la tarifa por segundo, cuántas
    comunicaciones se realizaron, y la duracion de cada
    comunicación expresada en horas, minutos y segundos. Como
    resultado se informa la duración en segundos de cada
    comunicación y su costo."""

    msj = """
    Llamada corta / tarifa : 30 minutos maximo / 0.5
    Llamada larga / tarifa : mayor o igual a 30 minutos / 0.75

    """
    print(msj)

    n = int(input("¿Cuántas comunicaciones hubo?: "))
    costoTotal = 0
    cllc = 0
    clll = 0
    tllc = 0
    tlll = 0
    for x in range(n):
        h = int(input("¿Cuántas horas?: "))
        m = int(input("¿Cuántos minutos?: "))
        s = int(input("¿Cuántos segundos?: "))
        duracion = a_segundos(h, m, s)
        p = calPrecio(duracion)
        costo = duracion * p
        pesos, centavos = pyc(costo)
        if duracion >= 1800:
            clll += 1
            tlll += costo
        else:
            cllc += 1
            tllc += costo
        print("Duracion:", duracion, "segundos. Costo: ",pesos,"Pesos con",centavos,"centavos.")
        costoTotal = costoTotal + costo
    pesosTotal, centavosTotal = pyc(costoTotal)
    pesosTotalllc, centavosTotalllc = pyc(tllc)
    pesosTotallll, centavosTotallll = pyc(tlll)
    msjF = f"""
        Costo Total LLamadas CORTAS: ",{pesosTotalllc} ,"Pesos con",{centavosTotalllc},"centavos.
        Costo Total LLamadas LARGAS: ",{pesosTotallll} ,"Pesos con",{centavosTotallll},"centavos.
        Costo Total: ",{pesosTotal} ,"Pesos con",{centavosTotal},"centavos.
    """
    print(msjF)

#e43
#Dados tres puntos en el plano expresados como coordenadas (𝑥, 𝑦) informar cuál
#es el que se encuentra más lejos del centro de coordenadas.

#Crear una funcion e43,luego creamos una lista vacia(ldis) dentro un ciclo con rango 3 (pedimos x,y).
# dentro del cuerpo del ciclo calculamos su distancia con la formula ; dis = raiz(x°2 + y°2)
# guardamos cada dis obtenida en la lista (ldis)
# Al terminar el ciclo obtenemos el mayor de la lista

def e43():
    ldis = []
    for i in range(3):
        x = int(input('X: '))
        y = int(input('Y: '))

        dis = sqrt(pow(x ,2) + pow(y ,2))
        ldis.append(dis)
    pm = max(ldis)
    msje = f"""
    El punto mas alejado del centro es el punto
    con una distancia de {pm}. 
    """
    print(msje)

def e43():
    dism = 0
    for i in range(3):
        x = int(input('X: '))
        y = int(input('Y: '))

        dis = sqrt(pow(x ,2) + pow(y ,2))
        ldis.append(dis)
    pm = max(ldis)
    msje = f"""
    El punto mas alejado del centro es el punto
    con una distancia de {pm}. 
    """
    print(msje)

myl = [10,1,9,2,8,3,7,4,6,5]
myl2 = {
    '1' : 'hola',
    '2' : 'hola2',
    '3' : 'hola3',
    '4' : 'hola4'
}
#EJERCICIOS 5X

#Nuevamente, se desea facturar el uso de un teléfono. Para ello se informa la tarifa
# por segundo y la duración de cada comunicación expresada en horas, minutos y segundos.
#Como resultado se informa la duración en segundos de cada llamado y su costo. Resolver este
# problema usando
#a. Un ciclo definido.
#b. Un ciclo interactivo.
#c. Un ciclo con centinela.
#d. Un ciclo “infinito” que se corta

#a. Un ciclo definido.
def e51a():
    tarifa = float(input('Precio por segundo: '))
    for i in range(2):
        h = int(input('Horas: '))
        m = int(input('Minutos: '))
        s = int(input('Segundos: '))
        dur = a_segundos(h, m, s)
        cent = dur * tarifa
        pesos, centavos = pyc(cent)
        msj = f"""
        Duracion: {dur}
        Precio : {pesos}Pesos con {centavos} centavos.
        """
        print(msj)

#b. Un ciclo interactivo.
def e51b():
    tarifa = float(input('Precio por segundo: '))
    r = 'Si'
    while r == 'Si':
        h = int(input('Horas: '))
        m = int(input('Minutos: '))
        s = int(input('Segundos: '))
        dur = a_segundos(h, m, s)
        cent = dur * tarifa
        pesos, centavos = pyc(cent)
        msj = f"""
        Duracion: {dur}
        Precio : {pesos}Pesos con {centavos} centavos.
        """
        print(msj)
        r = input('Otra llamada? <Si-No>')

#c. Un ciclo con centinela.
def e51c():
    tarifa = input('Precio por segundo("x" para terminar.): ')
    while tarifa != 'x':
        h = int(input('Horas: '))
        m = int(input('Minutos: '))
        s = int(input('Segundos: '))
        dur = a_segundos(h, m, s)
        tarifa = float(tarifa)
        cent = dur * tarifa
        pesos, centavos = pyc(cent)
        msj = f"""
        Duracion: {dur}
        Precio : {pesos}Pesos con {centavos} centavos.
        """
        print(msj)
        tarifa = input('Precio por segundo(X para terminar.): ')

#d. Un ciclo “infinito” que se corta

def e51d():
    while True:
        tarifa = input('Precio por segundo("x" para terminar.): ')
        if tarifa == 'x':
            break
        else:
            h = int(input('Horas: '))
            m = int(input('Minutos: '))
            s = int(input('Segundos: '))
            dur = a_segundos(h, m, s)
            tarifa = float(tarifa)
            cent = dur * tarifa
            pesos, centavos = pyc(cent)
            msj = f"""
            Duracion: {dur}
            Precio : {pesos}Pesos con {centavos} centavos.
            """
            print(msj)


#e574. Utilizando la función randrange del módulo random, escribir un programa que
#obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
#si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
#correcto.

from random import randrange

#Definimos la funcion e574
#Dentro de la funcion definimos un numero secreto(ns) con ayuda de randrange(nc)
#Crearemos un ciclo infinito
#Crearemos una estructura de decicsion, si el numero ingresado es igual al numero secreto cortaremos el ciclo.
#si es menor le diremos por msj que es menor
#lo mismo con mayor.

def e574():
    ns = randrange(1, 100)
    print(ns)
    while True:
        ni = int(input('Numero: '))
        if ni == ns:
            print(f'Felicidades!! Era {ns}')
            break
        if ni < ns:
            print(f'El Numero Secreto es MAYOR que {ni}')
        else:
            print(f'El Numero Secreto es MENOR que {ni}')



#e575
#a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
# números 𝑛 y 𝑚, dado por los siguientes pasos.
#1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
#2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
#3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.

#Parametros de entrada: dividendo y divisor (n,m)
#Valores de salida : 1 (mcd)
#Crearemos la funcion e575
#Pediremos los valores (n, m)

def e575():
    m = int(input('M: '))
    n = int(input('N: '))

    mcd = 0
    dividendo = 0 
    divisor = 0

    if m > n:
        dividendo = m
        divisor = n
    else:
        dividendo = n
        divisor = m
    
    while True:
        r = dividendo%divisor
        print(f'{dividendo}%{divisor}={r}')
        if r == 0:
            mcd = divisor
            print(f'MCD : {mcd}')
            break
        else:
            dividendo = divisor
            divisor = r
    

#e578 
#Escribir un programa que le pida al usuario que ingrese una sucesión de números
# naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición
# de salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma
# total de los valores y el promedio.

#Parametros de entrada : numeros indefinidos (hasta que decida el usuario.)
#Valores de salida : 3 : Cantidad de numeros(cn), suma total de numeros(sum), promedio(pr)
#Vamos a definir la funcion e578
#Definiermos un contador en 0
# Dentro crearemos un ciclo infinito hasta que ingrese -1
# en cada vuelta el contador incrementa en 1
# y vamos sumando los numeros

def e578():
    c = 0
    sum = 0
    while True:
        n = int(input('Ingrese numero: '))
        if n == -1:
            print(f'Contador: {c}.\nSuma: {sum}')
            break
        else:
            sum += n
            c +=1

#EJERCICIOS 6X

#e61 
#Escribir un ciclo que permita mostrar los caracteres de una cadena del final al principio.

def e61(palabra):
    for i in range(1, len(palabra)+1):
        print(palabra[-i])


#e64 
#Escribir una función contar(c, s) que cuente cuántas veces aparece un carácter c dado en una cadena s.

def e64(c, s):
    cr = 0
    for subcadena in c:
        if subcadena == s:
            cr+=1
    return cr


#e65.
#¿Hay más letras “A” o más letras “E” en una cadena? Escribir un programa que lo decida.

def e65(cadena):
    A = 0
    E = 0
    for letra in cadena:
        if letra == 'A':
            A+=1
        elif letra == 'E':
            E+=1
    if A > E:
        msj = f'Hay mas letras "A":{A}'
    elif E > A:
        msj = f'Hay mas letras "E":{E}'
    elif E == 0 and A == 0:
        msj = 'No hay letras A ni E'
    else:
        msj = f'Hay las mismas A Y E'
    return msj

#e66
#Escribir un programa que cuente cúantas veces aparecen cada una de las
# vocales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula.

vocales = 'aeiouAEIOU'


def e66(cadena):
    c = 0
    a, e, i, o, u = [0, 0, 0, 0, 0]

    for letra in cadena:
        if letra in vocales:
            c+=1
            if letra == 'a' or letra == 'A':
                a+=1
            elif letra == 'e' or letra == 'E':
                e+=1
            elif letra == 'i' or letra == 'I':
                i+=1
            elif letra == 'o' or letra == 'O':
                o+=1                                                
            elif letra == 'u' or letra == 'U':
                u+=1                
        else:
            continue
    msj = f"""
        Hay {c} vocales en {cadena}.
        a : {a}
        e : {e}
        i : {i}
        o : {o}
        u : {u}
    """
    return msj

# git remote add origin https://github.com/IvoPaitano/algEstrc.git
# git branch -M main
# git push -u origin main

#e62 juego MasterMind

import random

CANT_DIGITOS = 5
ME_DOY = 'me rindo'

def cod_random():
    digitos = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    codigo = ''
    for i in range(CANT_DIGITOS):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo

def analizar_propuesta(propuesta, codigo):
    aciertos = 0
    coincidencias = 0
    for i in range(CANT_DIGITOS):
        if propuesta[i] == codigo[i]:
            aciertos += 1
        elif propuesta[i] in codigo:
            coincidencias += 1
    return aciertos, coincidencias

def mastermind():
    codigo = cod_random()
    intentos = 0
    
    propuesta = input('Que codigo propones?')
    while codigo != propuesta and propuesta != ME_DOY:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print(f'Tu propuesta "{propuesta}" tiene {aciertos} aciertos y {coincidencias} coincidencias.')
        print(codigo)
        propuesta = input('Que codigo propones?')
    if propuesta == ME_DOY:
        msj = f'''Te rendiste con {intentos} intentos!!!
        El codigo era {codigo}!
        '''
    else:
        msj = f'''Felicidades, el codigo era "{codigo}"!!!
            Intentos : {intentos}.
        '''
    return msj

#e681 
# Escribir funciones que dada una cadena de caracteres:
#a) Imprima los dos primeros caracteres.
#b) Imprima los tres últimos caracteres.
#c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
#d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
#e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
#    'reflejoojelfer'.

def e681a(cadena):
    return cadena[:2]
def e681b(cadena):
    return cadena[-3:]
def e681c(cadena):
    res = ''
    for i in range(len(cadena)):
        if i%2==0:
            res += cadena[i]
    return res
def e681d(cadena):
    res = ''
    for i in range(1, len(cadena)+1):
        res += cadena[-i]
    return res
def e681e(cadena):
    inv = e681d(cadena)
    res = cadena + inv
    return res

#e682
#Escribir funciones que dada una cadena y un caracter:
#a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'
#b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_' debería devolver 'mi_archivo_de_texto.txt'
#c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y 'X' debería devolver 'su clave es: XXXX'
#d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'

def e682a(cadena):
    res = ''
    l = len(cadena)
    for i in range(l):
        if i == l-1:
            res += cadena[i]
        else:
            res += cadena[i]+','
    return res    
def e682b(cadena):
    #return cadena.replace(' ', '_')
    res = ''
    for i in range(len(cadena)):
        if cadena[i] == ' ':
            res += '_'
        else:
            res += cadena[i]
    return res

def e682c(cadena, c):
    l = len(cadena)
    res = l * c
    msj = f'su clave es : {res}'
    return msj

def e682d(cadena, c):
    res = ''
    l = len(cadena)
    for letra in range(l):
        if letra%3 == 2:
            res += cadena[letra]+'.'
        else:
            res += cadena[letra]
    return res

#e683
#Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar.
#Hay que pedir un parametro para la cantidad de veces a usar(vueltas), encerrar el cuerpo de la funcion entera en un ciclo con rango (vueltas)
# y cambiar el return por un print(respuesta), o agregar cada respuesta a un array y returnar un array al final del ciclo.

#684
#Escribir una función que reciba una cadena que contiene un largo número entero
# y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.


def e684(cadena):
    l = len(cadena)
    if l <=3:
        return cadena
    else:
        aux1 = cadena[:l%3]
        if len(aux1) == 0:
            part1 = ''
        elif len(aux1) <=3:
            part1 = aux1+'.'

        aux2 = cadena[l%3:]
        lpart2 = len(aux2)
        part2 = ''
        for i in range(lpart2):
            if i == lpart2-1:
                part2 += aux2[i]
            elif i%3 == 2:
                part2 += aux2[i]+'.'
            else:
                part2 += aux2[i]     
        return part1 + part2

#e685
#Escribir una función que dada una cadena de caracteres, devuelva:
#a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.
#b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina' debe devolver 'República Argentina'.
#c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer

def primerLetra(palabra):
    return palabra[:1]
def e685a(cadena):
    palabras = cadena.split()
    res = ''
    for palabra in palabras:
        p = primerLetra(palabra)
        res += p
    return res

def primerLetraMayuscula(palabra):
    res = ''
    mayuscula = palabra[:1].upper()
    resto = palabra[1:]
    res = mayuscula + resto
    return res

def e685b(cadena):
    palabras = cadena.split()
    res = []
    for palabra in palabras:
        res.append(primerLetraMayuscula(palabra))
    res = ' '.join(res)
    return res

def empiezaConA(palabra):
    if palabra[:1] == 'a' or palabra[:1] == 'A':
        return palabra
def e685c(cadena):
    palabras = cadena.split()
    res = []
    for palabra in palabras:
        if empiezaConA(palabra):
            res.append(palabra)
    res = ' '.join(res)
    return res

#e686
#Escribir funciones que dada una cadena de caracteres:
#a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver 'lgrtms'.
#b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe devolver 'i ooae'.
#c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe devolver '.
#d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def e686a(cadena):
    vocales = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u',]
    res = ''
    for letra in cadena:
        if letra not in vocales:
            res += letra
    return res
def e686b(cadena):
    vocales = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u',]
    res = ''
    for letra in cadena:
        if letra in vocales:
            res += letra
        elif letra == ' ':
            res += ' '
    return res
def e686b(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    res = ''
    for letra in cadena:
        if letra in vocales:
            if letra == 'a':
                res += 'e'
            if letra == 'e':
                res += 'i'
            if letra == 'i':
                res += 'o'
            if letra == 'o':
                res += 'u'
            if letra == 'u':
                res += 'a'                
        else:
            res += letra
    return res

def e686b(cadena):
    cadse = cadena.split()
    cadse = ''.join(cadse)
    f = len(cadse)
    msj = f'{cadena}, ES palindromo.'
    for i in range(f):
        if cadse[i] != cadse[-(i+1)]:
            msj = f'{cadena}, NO es palindromo.'
            break
    return msj

#e687
#Escribir funciones que dadas dos cadenas de caracteres:
#a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena' es una subcadena de 'subcadena'.
#b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome' debe devolver 'gnome'.

def e687a(cadena, subcadena):
    msj = f'"{subcadena}" NO es una subcadena de "{cadena}".'
    if subcadena in cadena:
        msj = f'"{subcadena}" ES una subcadena de "{cadena}".'
    return msj

def e687a(cadena, cadena2):
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    cadCorta = '' 
    cadLarga = ''
    res = ''
    if len(cadena) > len(cadena2):
        cadLarga = cadena 
        cadCorta = cadena2
    elif len(cadena) < len(cadena2):
        cadLarga = cadena2 
        cadCorta = cadena
    else:
        cadCorta = cadena
        cadLarga = cadena2 
    for i in range(len(cadCorta)):
        if cadCorta == cadLarga:
            res = f'"{cadCorta}" y "{cadLarga}" son IGUALES.'
            return res
        elif abecedario.index(cadCorta[i]) > abecedario.index(cadLarga[i]):
            res = cadLarga
            return res
        elif abecedario.index(cadCorta[i]) < abecedario.index(cadLarga[i]):
            res = cadCorta
            return res
        elif i == len(cadCorta)-1 and abecedario.index(cadCorta[i]) == abecedario.index(cadLarga[i]):
            res = cadCorta
            return res
        else:
            continue

#e688
#Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.

def e688(cadena):
    cin = cadena[::-1]
    res = 0
    for i in range(len(cin)):
        if cin[i] == '1':
            ac = pow(2, i)
            res += ac
    return res

#e689
#Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
# el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
# número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
# pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe devolver.

def pedirNumero():
    numero = input('Numero: ').strip()
    return numero
def e689(mensaje, min, max):
    print(mensaje)
    numero = pedirNumero()
    while True:
        auxNum = numero[1:]
        if numero.isnumeric() or auxNum.isnumeric():
            numero = int(numero)
            if numero in range(min, (max+1)):
                return numero
            else:
                numero = pedirNumero()
        else:
            numero = pedirNumero()
#EJERCICIOS 7X
#e73
#Cartas como tuplas.
#a) Proponer una representación con tuplas para las cartas de la baraja francesa.
#b) Escribir una función poker que reciba cinco cartas de la baraja francesa e informe (devuelva
#    el valor lógico correspondiente) si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo número).

def e73a():
    calificaciones = ('Pika', 'Corazon', 'Trebol', 'Diamante')
    valores = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K')
    baraja = []
    for i in range(len(calificaciones)):
        for j in range(len(valores)):
            auxTupla = [valores[j], calificaciones[i]]
            baraja.append(auxTupla)
    return tuple(baraja)

def traerCartas(baraja, c):
    from random import randint
    numeros = ()
    cartas = ()
    n = 0
    for i in range(c):
        while True:
            n = randint(0, 47)
            if n not in numeros:
                numeros += (n),
                cartas += (baraja[n]),
                break
    return cartas

def e73b(nCartas):
    import collections
    cartas = traerCartas(e73a(), nCartas)
    vCartas = ()
    msj = f'''
    {cartas}.
    No hay POKER
    '''
    for i in range(len(cartas)):
        vCartas += (cartas[i][0]),
    for i in range(len(vCartas)):
        if collections.Counter(vCartas)[vCartas[i]] >= (nCartas-1):
            msj = f'''
            {cartas}.
            HAY POKER.
            '''
            break
    return msj
        
#e74
#El tiempo como tuplas.
#a) Proponer una representación con tuplas para representar el tiempo.
#b) Escribir una función sumar_tiempos que reciba dos tiempos dados y devuelva su suma

def e74a(d,m,a):
    fecha = (d, m, a)
    return fecha

def e74b(tiempo1, tiempo2):
    tiempo1S = a_segundos(*tiempo1)
    tiempo2S = a_segundos(*tiempo2)
    suma = tiempo1S+tiempo2S
    res = e391b(suma)
    return res

#e75
#Escribir una función dia_siguiente que dada una fecha expresada como la terna (Día, Mes, Año) (donde Día, Mes y Año son números enteros) 
#calcule el día siguiente al dado, en el mismo formato.

def e75(d, m, a):
    meses = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12)
    de31 = (1, 3, 5, 7, 8, 10, 12)
    de30 = (4, 6, 9, 11)
    de28 = (2,)

    if d == 31 and m == 12:
        return ((d-30), (meses[m-12]), (a+1))
    elif d == 31 and (m in de31):
        return ((d-30), (meses[m]), (a))
    elif d == 30 and (m in de30):
        return ((d-29), (meses[m]), (a))
    elif d == 28 and (m in de28):
        return ((d-27), (meses[m]), (a))
    else:
        return ((d+1), (meses[m-1]), (a)) 
#e76
#Escribir una función dia_siguiente_m que dada una fecha expresada como la
# terna (Día, Mes, Año) (donde Día y Año son números enteros, y Mes es el texto "Ene", "Feb", …,"Dic", 
# según corresponda) calcule el día siguiente al dado, en el mismo formato.

def e76(d, mes, a):
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    de31 = ('Enero', 'Marzo', 'Mayo', 'Julio', 'Agosto', 'Octubre', 'Diciembre')
    de30 = ('Abril', 'Junio', 'Septiembre', 'Noviembre')
    de28 = ('Febrero',)

    if d == 31 and mes == 'Diciembre':
        return ((d-30), (meses[meses.index('Diciembre')-11]), (a+1))
    elif d == 31 and (mes in de31):
        return ((d-30), (meses[meses.index(mes)+1]), (a))
    elif d == 30 and (mes in de30):
        return ((d-29), (meses[meses.index(mes)+1]), (a))
    elif d == 28 and (mes in de28):
        return ((d-27), (meses[meses.index(mes)+1]), (a))
    else:
        return ((d+1), (mes), (a)) 

padrones = [78455, 78455, 79211, 54988, 66540, 47890]

def inscribir_alumnos():
    """Permite inscribir alumnos al curso"""
    print("Inscripcion en el curso de Algoritmos y Programación I")
    inscriptos = []
    while True:
        padron = int(input("Ingresa un padrón (<=0 para terminar): "))
        if padron <= 0:
            break
        if padron in inscriptos:
            print("El padrón ya está en la lista de inscriptos.")
            continue
        inscriptos.append(padron)
    return inscriptos


#e77
#Permitir que los alumnos se puedan inscribir o borrar.


def inscribir_alumnos77(inscriptos):
    """Permite inscribir alumnos al curso"""
    print("Inscripcion en el curso de Algoritmos y Programación I")
    while True:
        padron = int(input("Ingresa un padrón (<=0 para terminar): "))
        if padron <= 0:
            break
        if padron in inscriptos:
            print("El padrón ya está en la lista de inscriptos.")
            continue
        inscriptos.append(padron)
    return inscriptos

def borrar_alumnos(inscriptos):
    eliminados = []
    while True:
        padron = int(input('Ingrese padron a eliminar (<= 0 para terminar): '))
        if padron <= 0:
            break
        elif padron not in inscriptos:
            print(f'No existe el padron :{padron}.')
            continue
        elif padron in inscriptos:
            eliminados.append(padron)
            inscriptos.remove(padron)
            print(f'Eliminaste padron "{padron}"')
    print(f'Padrones eliminados: {eliminados}')
    return inscriptos


def e77():
    inscriptos = []
    while True:
        op = input('Bienvenido.\n1)Inscribir.\n2)Borrar.\n3)Ver lista.\n4)Salir.\nOpcion:')
        if op == '1':
            insc = inscribir_alumnos77(inscriptos)
            inscriptos + insc
        elif op == '2':
            inscriptos = borrar_alumnos(inscriptos)
        elif op == '3':
            print(inscriptos)
        elif op == '4':
            print('Saliendo...')
            break
        else:
            op = ''' Bienvenido.\n1)Inscribir.\n2)Borrar.\n3)Salir '''

#e78
#Inscribir y borrar alumnos como antes, pero registrar también el nombre y apellido

def inscribir_alumnos78(inscriptos, padrones):
    """Permite inscribir alumnos al curso"""
    print("Inscripcion en el curso de Algoritmos y Programación I")
    while True:
        padron = int(input("Ingresa un padrón (<=0 para terminar): "))
        if padron <= 0:
            break
        if padron in padrones:
            print("El padrón ya está en la lista de inscriptos.")
            continue
        if padron not in padrones:
            nombre = input("Ingresa nombre: ")
            apellido = input("Ingresa apellido: ")
            padrones.append(padron)
            alumno = [padron, nombre, apellido]
            inscriptos.append(alumno)
    return inscriptos

def borrar_alumnos78(inscriptos, padrones):
    eliminados = []
    while True:
        padron = int(input('Ingrese padron a eliminar (<= 0 para terminar): '))
        if padron <= 0:
            break
        elif padron not in padrones:
            print(f'No existe el padron :{padron}.')
            continue
        elif padron in padrones:
            i = padrones.index(padron)
            alumnoEliminado = inscriptos[i]
            eliminados.append(alumnoEliminado)
            padrones.remove(padron)
            inscriptos.pop(i)
            print(f'Eliminaste padron "{padron}"')
    print(f'Padrones eliminados: {eliminados}')
    return inscriptos

def e78():
    inscriptos = []
    padrones = []
    for inscripto in inscriptos:
        padrones.append(inscripto[0])
    while True:
        op = input('Bienvenido.\n1)Inscribir.\n2)Borrar.\n3)Ver lista.\n4)Salir.\nOpcion:')
        if op == '1':
            insc = inscribir_alumnos78(inscriptos, padrones)
            inscriptos + insc
        elif op == '2':
            inscriptos = borrar_alumnos78(inscriptos, padrones)
        elif op == '3':
            print(inscriptos)
        elif op == '4':
            print('Saliendo...')
            break
        else:
            op = ''' Bienvenido.\n1)Inscribir.\n2)Borrar.\n3)Salir '''


#e79
#Escribir una función que reciba como parámetro una cadena de palabras separadas
# por espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la cadena dada.

def e79(cadena):
    auxCadena = cadena.split()
    c = 0
    for palabra in auxCadena:
        if len(palabra) > 5:
            c += 1
    return c

def texto_limpio(texto):
    texto = texto.split()
    t_limpio = []
    for i,palabra in enumerate(texto):
        if palabra == '':
            continue
        elif '...' in palabra:
            t_limpio.append(palabra)
            continue
        elif palabra[-1] == '.':
            a, b = palabra[:-1], palabra[-1]
            t_limpio.append(a)
            t_limpio.append(b)
            continue
        else:
            t_limpio.append(palabra)
    if t_limpio[-1] != '.':
        t_limpio.append('.')
    return t_limpio

def es_corta(palabra,limitePalabra):
    return (len(palabra) <= limitePalabra)

def acortar_palabra(palabra, limitePalabra):
    return (palabra[:limitePalabra] + '@')

def e79(texto, limitePalabra, costoPalabraCorta, costoPalabraLarga):
    textolimpio = texto_limpio(texto)
    textoFinal = []
    costo = 0
    ultimaVuelta = len(textolimpio)-1
    for i, palabra in enumerate(textolimpio):
        if palabra == '.' and i == ultimaVuelta:
            textoFinal.append('STOPSTOP')
        elif palabra == '.':
            textoFinal.append('STOP')
        elif palabra == ',':
            textoFinal.append(palabra)
        elif es_corta(palabra, limitePalabra):
            costo += costoPalabraCorta
            textoFinal.append(palabra)
        else:
            costo += costoPalabraLarga
            palabra = acortar_palabra(palabra, limitePalabra)
            textoFinal.append(palabra)
    return texto,' '.join(textoFinal), costo

#e761
#Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.

def e761(tupla):
    tuplaOrdenada = sorted(list(tupla))
    return (tuplaOrdenada == list(tupla))

#762 Dominó.
#a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
#b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
#       Nota: utilizar la función split de las cadenas.

def e762a(tupla1, tupla2):
    a, b = tupla1
    return (a in (tupla2) or b in (tupla2))

def e762b(cadena):
    a,b = cadena.split()
    return (a[0] in b or a[2] in b)


#e763
#Campaña electoral
#a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje Estimado <nombre>, vote por mí.
#b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para 
#       los n nombres que se encuentran a partir de la posición p.
#c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, #para ello, deberán recibir una tupla de tuplas,
#        conteniendo el nombre y el género.


def e763a(nombres):
    for nombre in nombres:
        print(f'{nombre}, vote por mi.')

def e763b(nombres, p, n):
    soloEstos = nombres[(p-1):(p+n-1)]
    for nombre in soloEstos:
        print(f'{nombre}, vote por mi.')

nombres = (('nombre1','masculino'),('nombre2','femenino'),('nombre3','femenino'),('nombre4','femenino'),('nombre5','femenino'),('nombre6','masculino'),('nombre7','femenino'),('nombre8','masculino'))

def e763aInclusive(nembres):
    for nembre in nembres:
        if nembre[1] == 'masculino':
            print(f'Sr.{nembre[0]}, vote por mi.')
        else:
            print(f'Sra.{nembre[0]}, vote por mi.')

def e763bInclusive(nembres, p, n):
    soloEstes = nembres[(p-1):(p+n-1)]
    for nembre in soloEstes:
        if nembre[1] == 'masculino':
            print(f'Sr.{nembre[0]}, vote por mi.')
        else:
            print(f'Sra.{nembre[0]}, vote por mi.')

#e766
# Dada una lista de números enteros y un entero k, escribir una función que:
#a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
#b) Devuelva una lista con aquellos que son múltiplos de k.

def e766a(numeros, k):
    menores = []
    mayores = []
    iguales = []

    for numero in numeros:
        if numero < k:
            menores.append(numero)
        elif numero > k:
            mayores.append(numero)
        else:
            iguales.append(numero)
    return menores, mayores, iguales

def e766b(numeros, k):
    multiplos = []
    for numero in numeros:
        if not numero%k:
            multiplos.append(numero)
    return multiplos

#e767
#Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre)
# y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.

#lista = [('Paitano','Ivo','E'),('Simon','Diego','O'),('Nicolas','Aparicio','E'),('Mario','Paitano','D'),('Abigail','Martinez','L'),('Maria','Martinez','T')]

def e767(lista):
    nombres = []
    for datos in lista:
        nombreOrdenado = (datos[0],datos[2]+'.',datos[1])
        nombre = ' '.join(nombreOrdenado)
        nombres.append(nombre)
    return nombres

#e768
#Inversión de listas
#a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
#    Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
#b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.


#lista = ['Di', 'buen', 'día', 'a', 'papa']

def e768a(lista):
    invertida = []
    for i in range(1, len(lista)+1):
        invertida.append(lista[-i])
    return invertida

def e768b(lista):
    lim = len(lista)
    for i in range(lim):
        lista.append(lista[i])
    return lista[5:]

#e769
#Escribir una función empaquetar para una lista, donde epaquetar significa indicar
# la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).
#Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5,1), (1, 2), (3, 2)].

def empaquetar(lista):
    n = lista[0]
    c = 0
    i = 0
    res = []
    while i < len(lista):
        if n == lista[i]:
            c+=1
        else:
            auxTupla = (n, c)
            res.append(auxTupla)
            n = lista[i]
            c = 0
            i-=1
        i+=1
    ultimaTupla = (n, c)
    res.append(ultimaTupla)
    return res


def busqueda_binaria(lista, x):
    """Búsqueda binaria Precondición: la lista está ordenada Devuelve -1 si x no está en lista; Devuelve p tal que lista[p] == x, si x está en lista"""
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        print("[DEBUG]", "izq:", izq, "der:", der, "medio:", medio)
        if lista[medio] == x:
            # Encontramos el elemento; devolvemos su posición
            return medio
        if lista[medio] > x:
            # Seguimos buscando en el segmento de la izquierda
            der = medio - 1
        else:
            # Seguimos buscando en el segmento de la derecha
            izq = medio + 1
    # El valor no fue encontrado
    return -1


#e841
# Escribir una función que reciba una lista desordenada y un elemento, que:
#a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas.
#b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
#c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado por parámetro y devuelva una lista con las posiciones.

#listaDesordenada = ['a', 'e', 'b', 'error', '123', 'e', 'hola', '522', 'ivo', 'paitano', 'e']

def e841a(listaDesordenada, elemento):
    coincidentes = []
    coincidencias = 0
    for palabra in listaDesordenada:
        if palabra == elemento:
            coincidentes.append(palabra)
            coincidencias += 1
    return coincidentes, coincidencias

def e841b(listaDesordenada, elemento):
    indice = -1
    if elemento in listaDesordenada:
        indice = listaDesordenada.index(elemento)
        return indice
    else: 
        return indice

def e841c(listaDesordenada, elemento):
    pos = []
    while True:
        ind = e841b(listaDesordenada, elemento)
        if ind == -1:
            break
        else:
            pos.append(ind)
            inicio = ind + 1
            listaDesordenada = listaDesordenada[inicio:]
    return pos

#e842
# Escribir una función que reciba una lista de números no ordenada, que:
#a) Devuelva el valor máximo.
#b) Devuelva una tupla que incluya el valor máximo y su posición.
#c) ¿Qué sucede si los elementos son cadenas de caracteres?
# Nota: no utilizar lista.sort()

#listaNumeros = [61, 10, 2, 20, 30, 3, 5, 40, 4, 60, 43, 6]

def e842a(listaNumeros):
    maximo = listaNumeros[0]
    for numero in listaNumeros:
        if numero > maximo:
            maximo = numero
    return maximo

def e842b(listaNumeros):
    maximo = listaNumeros[0]
    indice = 0
    for i, numero in enumerate(listaNumeros):
        if numero > maximo:
            maximo = numero
            indice = i
    return indice, maximo

#def_e842c: Si los elementos son cadenas, en la coomparacion los convierto en numeros (int)



#e843
#Agenda simplificada
#Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista,
# todas las entradas que contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
#Debe devolver una lista con todas las tuplas encontradas.

#lista = [('Ivo Ezequiel Paitano', '11 6453 5377'), ('Ezequiel Martinez', '11 7753 5377'), ('Abigail Lucero Martinez', '11 1234 5678'), ('Mario Daniel', '11 8765 4321'), ('Diego Simon Hurtado', '11 2365 4871'), ('Nicolas Aparicio', '11 2365 1487'), ('Daniel Sosa', '11 6235 8497'), ('Esteban Amaya', '11 6532 5623'), ('Daniel Garcia', '11 2356 2154'), ('Cesar Olivera', '11 5292 8547'), ('Joel Efrain Rivero', '11 4578 1265')]
def e843(cadena, lista):
    res = []
    for nombre in lista:
        datos = nombre[0].split()
        for dato in datos:
            if cadena.lower() in dato.lower():
                res.append(nombre)
                break
    return res

#e844
#Sistema de facturación simplificado
#Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador, descripción, precio), y una lista de los productos a facturar,
# en la que cada uno consiste en una tupla de (identificador, cantidad).
#Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada producto comprado, y al final imprima el total general.
#Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

#Valores de entrada : listaProductos, listaFacturar
#Valores de salida : por C/P cantidad, descripcion{}, precio unitario y total;total general.

#productosOrdenados = [(1,'auriculares',6500),(2,'cooler',1500),(3,'disco duro',5000),(4,'disco solido',9000),(5,'gabinete',4800),(6,'microfono',1800),(7,'microprocesador',10000),(8,'monitor',15000),(9,'mouse',2500),(10,'parlantes',6500),(11,'placa de sonido',4700),(12,'placa de video',25000),(13,'placa madre',8500),(14,'ram',3200),(15,'teclado',1900)]
#listaFacturar = [(2,3),(4,4),(1000,1000),(8,1),(10,5),(2000,10),(14,2),(5,10)], listaSinProductos = [], listaError = [(20,3),(4000,4),(800,1),(100,5),(104,2),(50,10)]

def traerProducto(id):
    prod = f'Error, producto ID:"{id}" no existe.'
    for producto in productosOrdenados:
        idProducto = producto[0]
        if idProducto == id:
            prod = producto
            break
    return prod

def armarProducto(cantidad, descripcion, precioUnitario, precioTotal):
    prod = f'Cantidad:{cantidad} - Descripcion:{descripcion} - Precio Unitario:{precioUnitario} - Total:{precioTotal}.\n'
    return prod

def e844(productosOrdenados, listaFacturar):
    totalGeneral = 0
    prodError = []
    factura = ''
    ultimoProducto = len(listaFacturar)-1
    for indice, prod in enumerate(listaFacturar):
        id = prod[0]
        infoProducto = traerProducto(id)
        if type(infoProducto) is tuple:
            cant = prod[1]
            descr = infoProducto[1]
            preUni = infoProducto[2]
            preTot = cant * preUni
            prodCuenta = armarProducto(cant, descr, preUni, preTot)
            factura += prodCuenta
            totalGeneral += preTot
            if indice == ultimoProducto:
                factura += f'Total: {totalGeneral}'
        else:
            prodError.append(id)

    if len(factura) <= 0 and len(prodError) <= 0:
        factura = 'No introdujo ningun producto.'
    elif len(factura) <= 0 and len(prodError) >= 1:
        factura = f'No existen los productos con ID:{prodError}.'
    
    return factura


#e845.
#Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
# se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
# no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
#(No utilizar lista.sort().)

listaOrdenada = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,55,66,77,80,90,99,100,150,151,152,200,230,232,234,250]

def encontrarPosicion(lista, elemento):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq+der) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] > elemento:
            der = medio - 1
        else:
            izq = medio + 1
    return medio

def e845(listOrd, elemento):
    if elemento in listOrd:
        pos = encontrarPosicion(listOrd, elemento)
        return pos, listOrd
    else:
        pos = encontrarPosicion(listOrd, elemento)
        print(pos, listaOrdenada[pos])
        if elemento > listOrd[pos]:
            listOrd.insert(pos+1, elemento)
            return pos+1, listOrd
        else:
            listOrd.insert(pos, elemento)
            return pos, listOrd

inventario = [('The Art of Computer Programming, Volumes 1-4','Donald Knuth', 12, 179.62),('Concrete Mathematics: A Foundation for Computer Science','Donald Knuth', 5, 54.77),('The Pragmatic Programmer: From Journeyman to Master','Andrew Hunt and David Thomas', 3, 33.17),]

def total_libros_autor(inventario, autor_buscado):
    total = 0
    for titulo, autor, cantidad, precio in inventario:
        if autor == autor_buscado:
            total += cantidad
    return total

#Especiales 8X
#Dejamos como ejercicio implementar
# las funciones total_libros_autor, cantidad_poco_stock y titulos_caros en términos de map y filter.

#def segunAutor(autorp):
    #return [cantidad for titulo, autor, cantidad, precio in inventario if autorp == autor]

#def segunPrecio(preciop):
    #return [cantidad for titulo, autor, cantidad, precio in inventario if preciop == precio]

def cantidades_segun_criterio(criterio, valor):
    lista = []
    if criterio == 'titulo':
        for titulo, autor, cantidad, precio in inventario:
            if titulo == valor:
                lista.append(cantidad)
    elif criterio == 'autor':
        for titulo, autor, cantidad, precio in inventario:
            if autor == valor:
                lista.append(cantidad)
    elif criterio == 'cantidad':
        for titulo, autor, cantidad, precio in inventario:
            if cantidad == valor:
                lista.append(cantidad)                
    else:
        for titulo, autor, cantidad, precio in inventario:
            if precio == valor:
                lista.append(cantidad)                
    return lista

def etotal_libro_segun(criterio, valor):
    return sum(cantidades_segun_criterio(criterio, valor))

def probandoCosas(f):
    return sum(f)

#probandoCosas([cantidad for titulo, autor, cantidad, precio in inventario if autor == 'Donald Knuth'])

#e951
#Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas,
# y los valores una lista con los segundos.
l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días'), ('Hola', 'don Ivo'), ('Buenos', 'parlantes'), ('asd', 'que hace'), ('Hola', 'ante ultimo'), ('Buenos', 'Auriculares')]
def e951(lista_tuplas):
    dic = {}
    for clave, valor in lista_tuplas:
        if clave in dic:
            if type(dic[clave]) is list:
                dic[clave].append(valor)
            else:
                aux = [dic[clave]]
                aux.append(valor)   
                dic[clave] = aux
        else:
            dic[clave] = valor
    return dic


#952
#Diccionarios usados para contar.
#a)Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
#   hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
#b)Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario.
#c)Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.

cadena = 'Que lindo día que hace hoy'
easyCadena = 'abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjj'

def e952a(cadena):
    cadenaSplit = cadena.split()
    cadFinal = map(lambda palabra : palabra.lower(), cadenaSplit)
    dic = {}
    for palabra in cadFinal:
        if palabra not in dic:
            dic[palabra.lower()] = 1
        else:
            c = dic[palabra.lower()] + 1
            dic[palabra] = c
    return dic

def e952b(cadena):
    caracteres = list(easyCadena)
    dic = {}
    for caracter in caracteres:
        if caracter in dic:
            c = dic[caracter] + 1
            dic[caracter] = c
        else:
            dic[caracter] = 1
    return dic

#defe952c No entendi el enunciado, perdon u.u

#e953
#Continuación de la agenda.
#Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
#b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#El usuario puede utilizar la cadena ” * ”, para salir del programa.

agendaDic = {'Ivo Ezequiel Paitano':'11 6453 5377', 'Ezequiel Martinez':'11 7753 5377', 'Abigail Lucero Martinez':'11 1234 5678', 'Mario Daniel':'11 8765 4321', 'Diego Simon Hurtado':'11 2365 4871', 'Nicolas Aparicio':'11 2365 1487', 'Daniel Sosa':'11 6235 8497', 'Esteban Amaya':'11 6532 5623', 'Daniel Garcia':'11 2356 2154', 'Cesar Olivera':'11 5292 8547', 'Joel Efrain Rivero':'11 4578 1265'}

def e953(agenda):
    nombre = input('Ingrese nombre(" * ", para terminar.): ')
    while '*' not in nombre:
        if nombre in agenda:
            print(f'Telefono de "{nombre}": '+agenda[nombre]+'.\n1)Modificar.\n2)Continuar.\n')
            #Muestra el telefono y menu.
            op = int(input('Ingrese opcion:'))
            if op == 1:
                telefonoActualizado = input(f'Ingrese nuevo telefono para "{nombre}":')
                agenda[nombre] = telefonoActualizado
        else:
            nuevoTelefono = input(f'Ingrese telefono para "{nombre}": ')
            agenda[nombre] = nuevoTelefono
        nombre = input('Ingrese nombre(" * ", para terminar.): ')
    return agenda

#e954
# Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.

cadena = 'es un texto grande, gigante, y engorroso muy gegege.'
caracteresEspeciales = (',','.',':',' ')

def caracteresLimpios(cadena):
    caracteres = list(cadena)
    caracteres = filter(lambda caracter: caracter not in caracteresEspeciales, caracteres)
    caracteres = list(set(caracteres))
    caracteres.sort()
    return caracteres

def palabrasLimpias(cadena):
    palabras = cadena.split()
    res = []
    for palabra in palabras:
        if not palabra.isalnum():
            if palabra[0].isalnum():
                palabra=palabra[:len(palabra)-1]
            else:
                palabra=palabra[1:]
        res.append(palabra)
    return res
    
def limpiar(cadena, criterio):
    if criterio == 'caracter':
        return caracteresLimpios(cadena)
    else:
        return palabrasLimpias(cadena)

def filtrarPalabras(palabras, caracter):
    return [palabra for palabra in palabras if caracter in palabra]

def laMasLarga(palabras):
    #return list(map(lambda palabra: len(palabra), palabras)) -> con map.
    longitudes = [len(palabra) for palabra in palabras]
    mayor = longitudes.index(max(longitudes))
    masLarga = palabras[mayor]
    return masLarga


def e954(cadena):
    dic = {}
    caracteres = limpiar(cadena, 'caracter')
    palabras = limpiar(cadena, 'palabra')
    for caracter in caracteres:
        palabrasValidas = filtrarPalabras(palabras, caracter)
        palabraLarga = laMasLarga(palabrasValidas)
        dic[caracter] = palabraLarga

    return dic

dic = {'a':'1', 'b':'2','c':'3'}
dicarroba = {'a':'1', 'b':'2', 'c':'3', 'd':'4@', 'e':'5', 'f':'@6'}

def emails(diccionario):
    [print(f'El e-mail de {k} es {v}') for k,v in dic.items()]

def emailDic(diccionario):
    buenos = {k:v for k,v in diccionario.items() if '@' in v}
    return buenos

# with open('archivo.txt') as archivo:
#     for i, linea in enumerate(archivo):
#         print(i, linea.rstrip())

#e11101
# Escribir una función, llamada head que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

import os
def head(archivo, n):
    msj = ''
    ruta = os.path.join('archivos', 'archivo.txt')
    with open (ruta) as archivo:
        lineas = archivo.readlines()[0:n]
        for linea in lineas:
            msj+=linea
    return msj


#e11102
# Escribir una función, llamada cp, que copie todo el contenido de un archivo
#   (sea de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def cp(archivoCopiar, archivoCopia, esBinario):
    rutaCopiar = os.path.join('archivos', archivoCopiar)
    rutaCopia = os.path.join('archivos', archivoCopia)
    read = 'r'
    write = 'w'
    if esBinario:
        read += 'b'
        write += 'b'
    with open(rutaCopiar, read) as archivo:
        contenido = archivo.read()
        with open(rutaCopia, write) as archivoc:
            if esBinario:
                archivoc.write(contenido)
            else:
                archivoc.write(contenido+'\n')

#e11103
# Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
#   imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.


def imprimirlineas(archivo):
    ruta = os.path.join('archivos',archivo)
    especiales = ('\n',' ',',')
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        nl = str(len(lineas))

        archivo.seek(0)
        palabrasLineas = archivo.read()
        
        palabras = list(palabrasLineas.split())
        np = len(palabras)
        
        pal = list(palabrasLineas)
        caracteres = filter(lambda c: c not in especiales, pal)
        nc = len(list(caracteres))
    return nl, np, nc

#e11104
# Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima las líneas del archivo que contienen la cadena recibida.
def grep(cadena, archivo):
    #Crear una lista vacia
    #Necesito cada fila por separado
    #Buscar la cadena dentro de c/u - f.
    #   si está, guardar la fila en la lista creada previamente.
    #Finalmente retornar la lista.
    ruta = os.path.join('archivos', archivo)
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
    return [linea for linea in lineas if cadena in linea]

#e11.10.5
#Escribir una función, llamada rot13, que reciba un archivo de texto de origen
# y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
# en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido
# entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter.

abecedario = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4,'f':5,
              'g':6, 'h':7, 'i':8, 'j':9, 'k':10,'l':11,
              'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
              'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}

def cifrar(c):
    ni = (abecedario[c] + 13) % 26
    for i,v in abecedario.items():
        if v == ni:
            return i

def rot13(archivo, archivoCifrado):
    especiales = (',','',' ','.','0','1','2','3','4','5','6','7','8','9','\n')
    #De a-z comprenden un valor de 0-26, a dicho valor sumarle 13 y aplicar modulo 26.
    # se debe cifrar todo el texto, de modo que tenga la misma cantidad de lineas 
    ruta = os.path.join('archivos', archivo)
    rutaCifrado = os.path.join('archivos', archivoCifrado)
    contenido = []
    with open(ruta, 'r') as archivo:
    #Separar el contenido del mensaje por lineas
        lineas = archivo.readlines()
        #Crear un bucle con las linas ya separadas
        for linea in lineas:
            # Crear una cadena auxiliar
            cad = ''
            # separar cada linea por caracteres.
            caracteres = list(linea)
            #crear un ciclo para recorrer cada caracter
            for caracter in caracteres:
                #verificar que no sea un caracter especial
                if caracter not in especiales:
                    #aplicar a cada caracter el metodo de cifrado
                    caracter = cifrar(caracter)
                #sumar a la cadena auxiliar cada caracter 
                cad += str(caracter)
                #sumar a una lista vacia la cadena ya cifrada.
            contenido.append(cad)
    #Terminado el ciclo, agregamos la lista al archivo
    with open(rutaCifrado, 'w') as archivoc:
        archivoc.writelines(contenido)

#11106
# Persistencia de un diccionario
#a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
#    tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
#    y el segundo como diccionario.
#b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
#    y guarde el contenido del diccionario en el archivo, con el formato clave, valor

import csv
#recibe arhicov con clave y valor separados por ,(coma)
def cargar_datos(archivo):
    #Crear un diccionario vacio.
    diccionario = {}
    ruta = os.path.join('archivos', archivo)
    with open(ruta, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #Obtener los datos a partir de la 2da linea
        next(csv_reader)
        #Crear un ciclo sobre las lineas obtenidas
        for linea in csv_reader:
            #en cada iteracion agregar respectivamente clave y valor al diccionario
            diccionario[linea[0]] = linea[1]
    return diccionario

diccionariokv = {
    'uno':'1',
    'dos':'2',
    'tres':'3',
    'cuatro':'4',
    'cinco':'5',
    'seis':'6',
    'siete':'7',
    'ocho':'8',
    'nueve':'9',
} 

def guardar_datos(diccionario, archivo):
    ruta = os.path.join('archivos', archivo)
    lista = []
    with open(ruta, 'w', newline='') as new_file:
        #para escribir en archivos CSV
        csv_writer = csv.writer(new_file, delimiter=',')
        for key,value in diccionario.items():
            linea = (key,value)
            lista.append(linea)
        csv_writer.writerows(lista)


def modulo(vector):
    """Calcula el módulo de un vector.
    Pre: el vector es una secuencia de números.
    Post: Devuelve el módulo del vector."""
    if not vector:
        raise ValueError("El vector debe tener al menos dimensión 1")
    suma = 0
    for x in vector:
        if not isinstance(x, (int, float, complex)):
            raise TypeError("El vector debe contener valores numéricos")
        suma += x * x
    return suma ** 0.5

