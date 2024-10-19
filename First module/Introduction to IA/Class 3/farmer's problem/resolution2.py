from collections import deque

def es_estado_valido(r, z, p, m):
    """ Verifica si el estado es válido. """
    # No se puede dejar al zorro y al pollo juntos sin el robot
    if r != z and z == p:
        return False
    # No se puede dejar al pollo y al maíz juntos sin el robot
    if r != p and p == m:
        return False
    return True

def obtener_estados_siguientes(estado):
    """ Genera todos los posibles estados siguientes desde el estado actual """
    r, z, p, m = estado
    siguientes_estados = []
    
    # Define los movimientos posibles en función de la posición del robot
    posibles_movimientos = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1)]  # Robot solo, con zorro, con pollo, con maíz
    
    if r == 1:  # Si el robot está en la orilla opuesta, invierte los movimientos
        posibles_movimientos = [(-1, -z, -p, -m) for (r, z, p, m) in posibles_movimientos]
    
    for movimiento in posibles_movimientos:
        nuevo_r = r + movimiento[0]
        nuevo_z = z + movimiento[1]
        nuevo_p = p + movimiento[2]
        nuevo_m = m + movimiento[3]
        nuevo_estado = (nuevo_r, nuevo_z, nuevo_p, nuevo_m)
        if es_estado_valido(nuevo_r, nuevo_z, nuevo_p, nuevo_m):
            siguientes_estados.append(nuevo_estado)

    return siguientes_estados

def resolver_acertijo():
    """ Resuelve el problema del robot, el zorro, el pollo y el maíz utilizando BFS """
    estado_inicial = (0, 0, 0, 0)  # Robot, zorro, pollo, maíz en la orilla inicial
    estado_objetivo = (1, 1, 1, 1)  # Robot, zorro, pollo, maíz en la orilla opuesta
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
            r, z, p, m = paso
            print(f"Robot: {r}, Zorro: {z}, Pollo: {p}, Maíz: {m}")
    else:
        print("No se encontró una solución.")

# Resolver el acertijo
solucion = resolver_acertijo()
imprimir_solucion(solucion)
