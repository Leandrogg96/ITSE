from collections import deque

def es_estado_valido(m, c):
    """ Verifica si el estado es válido.
    No debe haber más caníbales que misioneros en cualquier lado del río,
    excepto cuando no haya misioneros en ese lado.
    """
    if m < 0 or m > 3 or c < 0 or c > 3: # Asegura que haya hasta 3 misioneros y canibales
        return False
    if m > 0 and m < c:  # Mas canibales que misioneros en el lado inicial
        return False
    #if (3 - m > 0) and (3 - m > 3 - c):  # Mas canibales que misioneros en el lado opuesto
     # return False
    return True

def obtener_estados_siguientes(estado):
    """ Genera todos los posibles estados siguientes desde el estado actual """
    m, c, bote = estado
    siguientes_estados = []
    
    # Define los movimientos posibles en funcion de la posicion del bote
    if bote == 1:  # Bote en el lado inicial
        posibles_movimientos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    else:  # Bote en el lado opuesto
        posibles_movimientos = [(-1, 0), (-2, 0), (0, -1), (0, -2), (-1, -1)]
    
    #for movimiento in posibles_movimientos:
    if m == c and m!=1:
        nuevo_m = m - posibles_movimientos[1][0]
        nuevo_c = c
    elif m > c:
        nuevo_m = m - posibles_movimientos[0][0]
        nuevo_c = c
    elif m < c:
        nuevo_c = c - posibles_movimientos[2][1]
        nuevo_m = m
    elif m < nuevo_c:
        nuevo_c = c - posibles_movimientos[3][1]
        nuevo_m = m
    elif m==c:    
        nuevo_m = m - posibles_movimientos[4][0]
        nuevo_c = c - posibles_movimientos[4][1]
    else:
        nuevo_c = c
        nuevo_m = m 
    nuevo_bote = 1 - bote  # Cambiar el lado del bote
    nuevo_estado = (nuevo_m, nuevo_c, nuevo_bote) # Movimiento
    if es_estado_valido(nuevo_m, nuevo_c):
        siguientes_estados.append(nuevo_estado)

    return siguientes_estados

def resolver_acertijo():
    """ Resuelve el problema de los misioneros y caníbales utilizando BFS """
    estado_inicial = (3, 3, 1)  # 3 misioneros, 3 caníbales, bote en el lado inicial
    estado_objetivo = (0, 0, 0)  # 0 misioneros, 0 caníbales, bote en el lado opuesto
    cola = deque([(estado_inicial, [])])
    visitados = set()
    
    while cola:
        estado_actual, camino = cola.popleft()
        
        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)
        
        if estado_actual == estado_objetivo:
            return camino + [estado_actual]
        
        for siguiente_estado in obtener_estados_siguientes(estado_actual):
            if siguiente_estado not in visitados:
                cola.append((siguiente_estado, camino + [estado_actual]))
    
    return None

def imprimir_solucion(solucion):
    """ Imprime los pasos de la solucion """
    if solucion:
        for paso in solucion:
            print(f"Misioneros: {paso[0]}, Canibales: {paso[1]}, Bote: {'Inicial' if paso[2] == 1 else 'Opuesto'}")
    else:
        print("No se encontro una solucion.")

# Resolver el acertijo
solucion = resolver_acertijo()
imprimir_solucion(solucion)
