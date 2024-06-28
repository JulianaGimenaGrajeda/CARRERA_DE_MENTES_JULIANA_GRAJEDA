'''
F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el score y dejar de mostrar las opciones.

G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si
agotó ambas opciones, deja de mostrar las opciones y no suma score

H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente
pregunta. También debe reiniciar el Score.
'''

'''
    HACER FUNCIONES PARA REUTILIZARLAS EN EL PARCIAL
'''

from datos import * 

def enlistar_datos(lista:list,clave:str):
    '''Toma los datos de una lista y los 
    agrega a otra en base a una clave
    parametro. Lista a trabajar, 
    clave de la cual se traeran los 
    datos.
    Retorno: Nueva lista con los datos.
    '''
    lista_nueva = []

    for dicc in lista:
        lista_nueva.append(dicc[clave])

    return lista_nueva

def cambiar_posicion(posicion,lista:str):
    '''Recibe un valor numérico, en este caso
    la posicion y aumenta su valor siempre
    y cuando sea menor al tamaño de una  lista
    menos 1.
    Parámetros: Posicion o valor numérico y
    lista a comparar.
    Retorno: Posicion con el valor sumado'''

    if posicion < len(lista)-1:
        posicion += 1
    return posicion