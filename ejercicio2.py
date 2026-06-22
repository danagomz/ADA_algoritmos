def camelcase(s):
    # Si por alguna razón la cadena está vacía, devolvemos 0
    if len(s) == 0:
        return 0

    # Como la primera palabra empieza en minúscula, inicializamos el contador en 1
    contador_palabras = 1

    # Recorremos cada letra de la cadena de texto
    for letra in s:
        # .isupper()-->función de Python que nos dice si una letra es MAYÚSCULA (True) o no (False)
        if letra.isupper():
            # Si es mayúscula, encontramos el inicio de una nueva palabra
            contador_palabras = contador_palabras + 1

    # Al terminar el ciclo, devolvemos el total de palabras encontradas
    return contador_palabras

print(camelcase("saveChangesInTheEditor"))  # Salida esperada: 5
print(camelcase("unoDosTres"))             # Salida esperada: 3