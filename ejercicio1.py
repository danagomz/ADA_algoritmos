#!/bin/python3

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    # Utilizamos sort con key=int para ordenar numéricamente
    # aunque los elementos sean strings. Esto es eficiente y 
    # evita errores de ordenamiento alfabético (ej. "10" antes de "2").
    unsorted.sort(key=int)
    return unsorted

if __name__ == '__main__':
    # Ejemplo de prueba manual directa para no escribir tanto en la terminal
    datos_prueba = ["31415926535897932384626433832795", "1", "3", "10", "3", "5"]
    print("Lista original:", datos_prueba)

    resultado = bigSorting(datos_prueba)
    print("Lista ordenada:", resultado)
