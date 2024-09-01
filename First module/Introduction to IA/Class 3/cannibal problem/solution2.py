from collections import deque

def es_estado_valido(m, c):
    """ Verifica si el estado es válido. No debe haber más caníbales que misioneros en cualquier lado del río,
    excepto cuando no haya misioneros en ese lado. """
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m > 0 and m < c:  # Más caníbales que misioneros en el lado inicial
        return False
    if (3 - m) > 0 and (3 - c) > (3 - m):  # Más caníbales que misioneros en el lado opuesto
        return False
    return True

def obtener_estados_siguientes(estado):
    """ Genera todos los posibles estados siguientes desde el estado actual """
    m, c, bote = estado
    siguientes_estados = []
    
    # Define los movimientos posibles en función de la posición del bote
    if bote == 1:  # Bote en el lado inicial
        posibles_movimientos = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    else:  # Bote en el lado opuesto
        posibles_movimientos = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
    
    # Generar estados en función de los movimientos posibles
    for movimiento in posibles_movimientos:
        nuevo_m = m - movimiento[0]
        nuevo_c = c - movimiento[1]
        nuevo_bote = 1 - bote  # Cambiar el lado del bote
        if es_estado_valido(nuevo_m, nuevo_c):
            siguiente_estado = (nuevo_m, nuevo_c, nuevo_bote)
            siguientes_estados.append(siguiente_estado)

    return siguientes_estados

def resolver_acertijo():
    """ Resuelve el problema de los misioneros y caníbales utilizando BFS y encuentra el camino más corto """
    estado_inicial = (3, 3, 1)  # 3 misioneros, 3 caníbales, bote en el lado inicial
    estado_objetivo = (0, 0, 0)  # 0 misioneros, 0 caníbales, bote en el lado opuesto
    cola = deque([(estado_inicial, [])])
    visitados = set()
    
    while cola:
        estado_actual, camino = cola.popleft()
        
        if estado_actual == estado_objetivo:
            return camino + [estado_actual]
        
        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)
        
        for siguiente_estado in obtener_estados_siguientes(estado_actual):
            if siguiente_estado not in visitados:
                cola.append((siguiente_estado, camino + [estado_actual]))
    
    return None

def imprimir_solucion(solucion):
    """ Imprime los pasos de la solución """
    if solucion:
        for paso in solucion:
            print(f"Misioneros: {paso[0]}, Caníbales: {paso[1]}, Bote: {'Inicial' if paso[2] == 1 else 'Opuesto'}")
    else:
        print("No se encontró una solución.")

# Resolver el acertijo
solucion = resolver_acertijo()
imprimir_solucion(solucion)
