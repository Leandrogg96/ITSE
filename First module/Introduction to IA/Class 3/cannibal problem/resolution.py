from collections import deque

# Establecer reglas (estados posibles valido)
def is_valid_state(m, c, b):
    # Validar que el estado sea seguro y posible
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

# Obtener un nuevo estado
def get_next_states(m, c, b):
    next_states = []
    # Posibles movimientos con la barca de 1 o 2 personas
    if b == 0:  # Barco en el lado inicial
        if m >= 2:
            next_states.append((m - 2, c, 1))
        if m >= 1:
            next_states.append((m - 1, c, 1))
        if c >= 2:
            next_states.append((m, c - 2, 1))
        if c >= 1:
            next_states.append((m, c - 1, 1))
        if m >= 1 and c >= 1:
            next_states.append((m - 1, c - 1, 1))
    else:  # Barco en el lado opuesto
        if (3 - m) >= 2:
            next_states.append((m + 2, c, 0))
        if (3 - m) >= 1:
            next_states.append((m + 1, c, 0))
        if (3 - c) >= 2:
            next_states.append((m, c + 2, 0))
        if (3 - c) >= 1:
            next_states.append((m, c + 1, 0))
        if (3 - m) >= 1 and (3 - c) >= 1:
            next_states.append((m + 1, c + 1, 0))
    return [state for state in next_states if is_valid_state(*state)]

# Aplicar metodo de resolcion
def bfs_solve():
    initial_state = (3, 3, 0)  # (misioneros en la orilla inicial, caníbales en la orilla inicial, posicion del barco)
    goal_state = (0, 0, 1)  # Todos deben estar en el lado opuesto y el barco tambien
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal_state:
            return path + [(m, c, b)]

        if (m, c, b) in visited:
            continue

        visited.add((m, c, b))

        for next_state in get_next_states(m, c, b):
            if next_state not in visited:
                # Añade el siguiente estado a la cola con el nuevo camino
                queue.append((next_state, path + [(m, c, b)]))

    return None  # No se encontro solucion

# Ejecutar la busqueda
solution = bfs_solve()
if solution:
    print("Solucion encontrada:")
    for step in solution:
        print(step)
else:
    print("No se encontro solucion")
