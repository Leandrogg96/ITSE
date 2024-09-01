from collections import deque 

""" Misioneros y canibales
    En el acertijo de los misioneros y los canibales, tres misioneros y tres canibales tienen que cruzar un rio con una barca 
que solo puede llevar como maximo dos personas, lo cual es un constrenimiento para ambos bandos, porque 
si hay misioneros presentes en el barco, los canibales se comerian a los misioneros. La barca no puede cruzar por el rio 
sin personas a bordo. A tener en cuenta:

- No puede haber mas canibales que misioneros en ningun momento (las personas sobre la barca cuentan)
- La barca nunca puede volver vacia

"""
def es_estado_valido(m, c):
    """ Verifica si el estado es valido. No debe haber mas canibales que misioneros en cualquier lado del rio,
    excepto cuando no haya misioneros en ese lado. """
    if m < 0 or m > 3 or c < 0 or c > 3:  # Asegura que haya hasta 3 misioneros y canibales
        return False
    if m > 0 and m < c:  # Mas canibales que misioneros en el lado inicial
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):  # Mas canibales que misioneros en el lado opuesto
        return False
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
    
    # Generar estados en funcion de los movimientos posibles
    for movimiento in posibles_movimientos:
        nuevo_m = m - movimiento[0]
        nuevo_c = c - movimiento[1]
        nuevo_bote = 1 - bote  # Cambiar el lado del bote
        nuevo_estado = (nuevo_m, nuevo_c, nuevo_bote)
        if es_estado_valido(nuevo_m, nuevo_c):
            siguientes_estados.append(nuevo_estado)

    return siguientes_estados

def resolver_acertijo():
    """ Resuelve el problema de los misioneros y canibales utilizando BFS (Breadth First Search)"""
    estado_inicial = (3, 3, 1)  # 3 misioneros, 3 canibales, bote en el lado inicial
    estado_objetivo = (0, 0, 0)  # 0 misioneros, 0 canibales, bote en el lado opuesto
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
            print(f"Misioneros: {paso[0]}, Canibales: {paso[1]}, Bote: {'Inicial' if paso[2] == 1 else 'Opuesto'} ")
    else:
        print("No se encontro una solucion.")

# Resolver el acertijo
solucion = resolver_acertijo()
imprimir_solucion(solucion)
