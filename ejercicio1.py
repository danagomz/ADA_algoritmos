def bigSorting(V, arr):
    # Recorremos el arreglo elemento por elemento junto con su posición (índice)
    for i in range(len(arr)):
        # Si encontramos el valor que estamos buscando
        if arr[i] == V:
            # Devolvemos el índice exacto donde se encuentra
            return i

    # Si por alguna razón no se encuentra, devolvemos -1
    return -1

# --- Pruebas de funcionamiento (Ejemplo estándar de HackerRank) ---
# Buscamos el número 4 en un arreglo ordenado
valor_buscado = 4
arreglo_ejemplo = [1, 4, 5, 7, 9, 12]

resultado = bigSorting(valor_buscado, arreglo_ejemplo)
print(f"El valor {valor_buscado} se encuentra en el índice: {resultado}")
# Salida esperada: El valor 4 se encuentra en el índice: 1