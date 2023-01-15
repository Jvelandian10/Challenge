# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    #Tu código aca:
    list = []
    multiplica= 1
    numero1 = numero * multiplica
    while numero1 <= tope:
     list.append(numero1)
     multiplica += 1
     numero1 = numero * multiplica
    
    return list

print (ListaDivisibles(6, 30))
print (ListaDivisibles(10, 5))
print (ListaDivisibles(7, 50))
    
def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    #Tu código aca:
    return numero ** exponente

print (Exponente(10, 3))

def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
   
    if not (isinstance(lista, list)):
        return None   


    copia1 = lista.copy()
    resultado = []
    while len(copia1) > 0:
        current = copia1.pop(0)
        if isinstance(current, int) or isinstance(current, str):
            resultado.append(current)

        if isinstance(current, list):
            for i in range(len(current) - 1, -1, -1):
              copia1.insert(0, current[i])

        if len(copia1) == 0:
            return resultado

print(ListaDeListas([1,2,['a','b'],[10]]))
print(ListaDeListas(108))
print(ListaDeListas([[1,2,[3]],[4]]))
    

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    #Tu código aca:
   
    if numero < 0:
        return None
    if numero == 0 :
        return 1
    
    return numero * Factorial (numero - 1)

print(Factorial(4))
print(Factorial(-2))
print(Factorial(0))

def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea menor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    #Tu código aca:
    
    if (not (isinstance(desde, int))) or (not (isinstance(hasta, int))):
        return None
    if desde < 0 or hasta < 0:
        return None
    # Determinacion de que si es primo
    def isPrime(n):
        # Se considera 1 primo y no es asi
        if n == 1:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    Lista2 = []
    for i in range(desde, hasta + 1):
        if isPrime(i):
            Lista2.append(i)
    return Lista2

print(ListaPrimos(7,15))
print(ListaPrimos(100,99))
print(ListaPrimos(1,7))


def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
    '''
    #Tu código aca:
   
    if not (type(lista) is list):
        return None

    frequencyCounter = {}

    for i in lista:
        key = ""
        if isinstance(i, str):
            key = i

        elif isinstance(i, int):
            key = str(i)

        if key in frequencyCounter.keys():
            frequencyCounter[key] += 1
        else:
            frequencyCounter[key] = 1

    Lista3 = []
    for key in frequencyCounter.keys():
        if key.isdigit():
            newTupple = (int(key), frequencyCounter[key])
            Lista3.append(newTupple)
        else:
            newTupple = (key, frequencyCounter[key])
            Lista3.append(newTupple)

    return Lista3


print(ListaRepetidos([]))
print(ListaRepetidos(["hola", "mundo", "hola", 13, 14]))
print(ListaRepetidos([1, 2, 2, 4]))

def ClaseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:
        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    y debe tener el siguiente método:
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    #Tu código aca:
    class Vehiculo:
        def __init__(self, tipo: str, color: str):
            self.Tipo = tipo
            self.Color = color
            self.Velocidad = float(0)

        def Acelerar(self, delta):
            newVelo = self.Velocidad + delta
            if newVelo < 0:
                self.Velocidad = 0
            elif newVelo > 100:
                self.Velocidad = 100
            else:
                self.Velocidad = newVelo
            return self.Velocidad

    newVehicle = Vehiculo(tipo, color)

    return newVehicle


a = ClaseVehiculo("auto", "gris")
print(a.Acelerar(10))
print(a.Acelerar(15))
print(a.Acelerar(-10))

def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    if not (type(diccionario_par) is dict):
        return None
    if not (clave in diccionario_par.keys()):
        return None

    # verificamos si las claves poseen al menos un valor:
    cantValores = 0
    lista4 = []
    Lista5a = []

    res = {}

    if len(diccionario_par[list(diccionario_par.keys())[0]]) > 0:
        cantValores = len(diccionario_par[list(diccionario_par.keys())[0]])
        # Diccionario en listas
        for i in range(0, cantValores):
            Objete1 = {}
            for key in diccionario_par:
                Objete1[key] = diccionario_par[key][i]
            lista4.append(Objete1)
        # Se trata de ordenar
        Lista5a = sorted(lista4, key=lambda d: d[clave], reverse=not (descendente))
        # print(newArrSorted)
        # Lista de diccionarios
        for key in diccionario_par:
            lista6 = []
            for i in range(0, cantValores):
                lista6.append(Lista5a[i][key])
            res[key] = lista6
    # Si no se encuentra volvemos
    else:
        return diccionario_par

    return res


dicc = {
    "clave1": ["c", "a", "b"],
    "clave2": ["casa", "auto", "barco"],
    "clave3": [1, 2, 3],
}

OrdenarDiccionario(dicc, "clave1")
print(OrdenarDiccionario(dicc, "clave3", False))
    