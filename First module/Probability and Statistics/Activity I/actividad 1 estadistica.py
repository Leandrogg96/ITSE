import numpy as np
import pandas as pd
from tabulate import tabulate

# Datos
notas = [
    3, 4, 6, 7, 9, 3, 2, 3, 6, 2, 3, 3, 2, 7, 5, 6, 5, 5, 1, 4, 2, 8, 7, 6, 8, 7, 4, 8, 2, 10,
    7, 7, 4, 6, 8, 4, 6, 8, 6, 1, 8, 6, 5, 10, 4, 5, 9, 6, 5, 1, 8, 7, 9, 8, 5, 7, 6, 9, 7, 7
]

# Notas
familias_notas = list(range(1, 11))

# Calculo de la frecuencia absoluta
frecuencia_absoluta = np.bincount(notas)[1:]  # ignoramos el 0


# Calculo de la frecuencia absoluta acumulada
frecuencia_absoluta_acumulada = np.cumsum(frecuencia_absoluta).round(3)

# Calculo de la frecuencia relativa
frecuencia_relativa = (frecuencia_absoluta / len(notas)).round(3)

# Calculo de la frecuencia relativa acumulada
frecuencia_relativa_acumulada = np.cumsum(frecuencia_relativa).round(3)

# Calculo de la frecuencia porcentual
frecuencia_porcentual = (frecuencia_relativa * 100).round(3)

# Calculo de la frecuencia porcentual acumulada
frecuencia_porcentual_acumulada = np.cumsum(frecuencia_porcentual).round(3)

# Creo un DataFrame para organizar los resultados
tabla_frecuencias_absolutas = pd.DataFrame({
    'Nota': familias_notas,
    'Frecuencia Absoluta': frecuencia_absoluta,
    'Frecuencia Absoluta Acumulada': frecuencia_absoluta_acumulada
})

tabla_frecuencias_relativas = pd.DataFrame({
    'Nota': familias_notas,
    'Frecuencia Relativa': frecuencia_relativa,
    'Frecuencia Relativa Acumulada': frecuencia_relativa_acumulada
})

tabla_frecuencias_porcentuales = pd.DataFrame({
    'Nota': familias_notas,
    'Frecuencia Porcentual (%)': frecuencia_porcentual,
    'Frecuencia Porcentual Acumulada (%)': frecuencia_porcentual_acumulada
})

print(tabulate(tabla_frecuencias_absolutas, headers='keys', tablefmt='pretty'))
print(tabulate(tabla_frecuencias_relativas, headers='keys', tablefmt='pretty'))
print(tabulate(tabla_frecuencias_porcentuales, headers='keys', tablefmt='pretty'))


