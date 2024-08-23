import numpy as np
import pandas as pd
from tabulate import tabulate

"""
p = [False, True]
no_p = [not i for i in p]

print(p)
print(no_p)
"""

datos = pd.read_excel('C:/Users/julie/OneDrive - Universidad Católica de Santiago del Estero/Escritorio/ITSE/First module/Math/Class 2/Activity 1/class_activity_1.xlsx')
tabla = tabulate(datos, headers='keys', tablefmt='pretty')
print(tabla)

def negacion(*args):
    return print([not i for i in args])

negacion(True, False, True, False)

def _negacion(booleanos):
    return print([0 if i else 1 for i in booleanos])

_negacion([True, False, True, False, False, True])

#Creando tabla

cantidad_alumnos = 70

asistencia_reunion = np.random.choice(['Si', 'No'], size=cantidad_alumnos)
participacion_activa = np.random.choice(['Si', 'No'], size=cantidad_alumnos)

planilla = pd.DataFrame({
    'Asistencia a la reunion': asistencia_reunion,
    'Participó activamente': participacion_activa
})

planilla_tabulada = tabulate(planilla, headers='keys', tablefmt='pretty')
print(planilla_tabulada)

planilla['Asistencia y participacion'] = (
    (planilla['Asistencia a la reunion'] == 'Si') & 
    (planilla['Participó activamente'] == 'Si')
)

planilla_tabulada = tabulate(planilla, headers='keys', tablefmt='pretty')
print(planilla_tabulada)

planilla["Asistencia o participacion"] = (
    (planilla['Asistencia a la reunion'] == 'Si') |
    (planilla['Participó activamente'] == 'Si')
)

planilla_tabulada = tabulate(planilla, headers='keys', tablefmt='pretty')
print(planilla_tabulada)

def contar_verdaderos(df, columna):
    return df[columna].sum()

cantidad_asistencia_y_participacion = contar_verdaderos(planilla, 'Asistencia y participacion')
print(f'\nCantidad de alumnos que asistieron y participaron: {cantidad_asistencia_y_participacion}')

cantidad_asistencia_o_participacion = contar_verdaderos(planilla, 'Asistencia o participacion')
print(f'\nCantidad de alumnos que asistieron o participaron: {cantidad_asistencia_o_participacion}')
