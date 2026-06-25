import math
import os
import random
import re
import sys

def camelcase(s):
    # Si la cadena está vacía, no hay palabras [cite: 1]
    if len(s) == 0:
        return 0

    # Inicializamos en 1 porque la primera palabra empieza en minúscula [cite: 1]
    contador_palabras = 1

    # Recorremos cada letra buscando mayúsculas [cite: 1]
    for letra in s:
        # Si la letra es mayúscula, significa que inicia una nueva palabra [cite: 2]
        if letra.isupper():
            contador_palabras += 1

    return contador_palabras

if __name__ == '__main__':

    s = input("Ingresa la palabra en camelCase: ")
    result = camelcase(s)
    print(f"Número de palabras: {result}")