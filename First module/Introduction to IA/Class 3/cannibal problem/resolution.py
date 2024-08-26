from collections import deque

def is_valid_state(m, c, b):
    # Validar que el estado sea seguro y posible
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    # Verificar que los misioneros no sean superados por caníbales en ningún lado
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def get_next_states(m, c, b):
    next_states = []
    if b == 0:  # Barco en el lado inicial
        # Movimiento de la barca de 1 o 2 personas desde el lado inicial al lado opuesto
        if m >= 2:
            next_states.append((m - 2, c, 1))  # Dos misioneros cruzan
        if m >= 1:
            next_states.append((m - 1, c, 1))  # Un misionero cruza
        if c >= 2:
            next_states.append((m, c - 2, 1))  # Dos caníbales cruzan
        if c >= 1:
            next_states.append((m, c - 1, 1))  # Un caníbal cruza
        if m >= 1 and c >= 1:
            next_states.append((m - 1, c - 1, 1))  # Un misionero y un caníbal cruzan
    else:  # Barco en el lado opuesto
        # Movimiento de la barca de 1 o 2 personas desde el lado opuesto al lado inicial
        if (3 - m) >= 2:
            next_states.append((m + 2, c, 0))  # Dos misioneros regresan
        if (3 - m) >= 1:
            next_states.append((m + 1, c, 0))  # Un misionero regresa
        if (3 - c) >= 2:
            next_states.append((m, c + 2, 0))  # Dos caníbales regresan
        if (3 - c) >= 1:
            next_states.append((m, c + 1, 0))  # Un caníbal regresa
        if (3 - m) >= 1 and (3 - c) >= 1:
            next_states.append((m + 1, c + 1, 0))  # Un misionero y un caníbal regresan
    return [state for state in next_states if is_valid_state(*state)]

def bfs_solve():
    initial_state = (3, 3, 0)  # (misioneros en la orilla inicial, caníbales en la orilla inicial, posición del barco)
    goal_state = (0, 0, 1)  # Todos deben estar en el lado opuesto y el barco también
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

    return None  # No se encontró solución

# Ejecutar la búsqueda
solution = bfs_solve()
if solution:
    print("Solución encontrada:")
    for step in solution:
        print(step)
else:
    print("No se encontró solución")
