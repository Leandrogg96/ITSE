from collections import deque

def is_valid(state):
    # Verificar el estado valido
    granjero, zorro, gallina, maiz = state
    # No valido si el zorro y la gallina estan solos juntos sin el granjero
    if zorro == gallina and granjero != zorro:
        return False
    # No valido si la gallina y el maíz estan solos juntos sin el granjero
    if gallina == maiz and granjero != gallina:
        return False
    return True

def get_next_states(state):
    granjero, zorro, gallina, maiz = state
    next_states = []
    # Posibles movimientos del granjero
    moves = [
        ('L', 'R'),  # de izquierda a derecha
        ('R', 'L')   # de derecha a izquierda
    ]
    for move in moves:
        # Granjero viaja solo
        new_state = (move[1] if granjero == move[0] else move[0], zorro, gallina, maiz)
        if is_valid(new_state):
            next_states.append(new_state)
        # Granjero viaja con zorro
        if granjero == zorro:
            new_state = (move[1] if granjero == move[0] else move[0], move[1] if zorro == move[0] else move[0], gallina, maiz)
            if is_valid(new_state):
                next_states.append(new_state)
        # Granjero viaja con gallina
        if granjero == gallina:
            new_state = (move[1] if granjero == move[0] else move[0], zorro, move[1] if gallina == move[0] else move[0], maiz)
            if is_valid(new_state):
                next_states.append(new_state)
        # Granjero viaja con maíz
        if granjero == maiz:
            new_state = (move[1] if granjero == move[0] else move[0], zorro, gallina, move[1] if maiz == move[0] else move[0])
            if is_valid(new_state):
                next_states.append(new_state)
    return next_states

def solve(initial_state = ('L', 'L', 'L', 'R')):  # Por defecto todos empiezan en el lado izquierdo
    goal_state = ('R', 'R', 'R', 'R')     # Todos deben terminar en el lado derecho
    queue = deque([(initial_state, [])])  # Cola de estados por explorar
    visited = set()  # Conjunto de estados visitados

    while queue:    
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                # Añade el siguiente estado a la cola con el nuevo camino
                queue.append((next_state, path + [current_state]))

    return None  # No hay solucion

def get_initial_state():
    while True:
        user_input = input("Ingrese el estado inicial (granjero, zorro, gallina, maiz) en formato 'L' o 'R', separado por comas (ejemplo: L,L,L,L). Donde: \n # 'L': Lado izquiero del rio.\n # 'R': Lado derecho del rio.\n").strip()
        parts = user_input.split(',')
        if len(parts) != 4 or not all(part in ('L', 'R') for part in parts):
            print("Entrada invalida. Asegurese de ingresar 4 valores separados por comas, cada uno siendo 'L' o 'R'.")
            continue
        initial_state = tuple(parts)
        if not is_valid(initial_state):
            print("El estado inicial no es valido segun las reglas del acertijo.")
            continue
        return initial_state

if __name__ == "__main__":
    print("Bienvenido al acertijo del Granjero! Sere tu asistente y te ayudare a encontrar el camino ideal.")
    print("Te recuerdo que las reglas son simples.\n # Se parte de del lado izquiero de un rio y deben llegar todos al lado derecho.")
    print(" # Existe dos estados no validos.\n  1. El zorro y la gallina no pueden quedar solos sin el granjero.")
    print("  2. La gallina y el maiz no pueden quedar solos sin el granjero.")
    print("Para encontrar la solucion tendras que ingresar un estado inicial.")
    initial_state = get_initial_state()
    solution = solve(initial_state)

    if solution:
        print("Solucion encontrada:")
        for step in solution:
            print(step)
    else:
        print("No pude encontrar un camino posible. Lo siento, no existe una posible solucion.")
