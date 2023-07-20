"""
     Vectores
        a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
        b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
        c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
        d) Escribir una función que reciba un vector y devuelva su norma.

"""
import math

def producto_escalar(vector1,vector2):
    # Recibe dos vectores (en forma de tupla) y devuelva su producto escalar
    resultado = 0

    for i in range(len(vector1)):
        resultado = resultado + (vector1[i] * vector2[i])

    return resultado



def es_ortogonal(vector1,vector2):
    # Recibe dos vectores (en forma de tupla) y devuelva si son o no ortogonales
    resultado = 0
    condicion = False

    for i in range(len(vector1)):
        resultado = resultado + (vector1[i] * vector2[i])

    if resultado == 0:
        condicion = True

    return condicion


def es_paralelo(vector1,vector2):
    # Recibe dos vectores (en forma de tupla) y devuelva si son paralelos o no

    longitud = len(vector1) - 1
    condicion = True
    i = 0
    num1 = vector1[i]/vector2[i] # division de las primeras posiciones de los vectores

    while i<longitud and condicion:
        num2 = vector1[i+1]/vector2[i+1] # division de las posiciones siguientes de los vectores

        if num1 != num2:
            condicion = False
        else:
            num1 = num2
            i+=1

    return condicion

# print(es_paralelo((1,-2,4),(-2,4,-8)))
# print(es_paralelo((1,-2,4),(-2,4,-2)))


def norma_vector(vector1):
    # Recibe un vector (en forma de tupla) y devuelve su norma

    resultado = 0

    for i in range(len(vector1)):

        resultado = resultado + (vector1[i]**2)

    resultado = math.sqrt(resultado)

    return resultado


# print(norma_vector((2,5,4)))