def bellman_ford(vertices, arestas, origem):
    dist = {v: float('inf') for v in vertices}
    pred = {v: None for v in vertices}
    dist[origem] = 0

    for i in range(len(vertices) - 1):
        # print(f"Iteração {i+1}:")
        for u, v, p in arestas:
            # print(f'{dist}\n{pred}\n')
            if dist[u] + p < dist[v]:
                dist[v] = dist[u] + p
                pred[v] = u

    for u, v, p in arestas:
        if dist[u] + p < dist[v]:
            # print("\nCiclo negativo")
            return None, None

    return dist, pred


if __name__ == '__main__':
    vertices = {'S', 'A', 'B', 'C', 'D'}

    arestas = [
        ('S', 'A', 3),
        ('S', 'B', 5),
        ('S', 'D', 2),
        ('B', 'A', 6),
        ('B', 'C', 8),
        ('B', 'D', -9),
        ('A', 'C', -5),
        ('A', 'D', 8),
        ('C', 'D', -3)
    ]

    dist, pred = bellman_ford(vertices, arestas, 'S')

    if dist:
        print("Resultado: ")
        for v in vertices:
            print(f"Distância[{v}] = {dist[v]} | Predecessor = {pred[v]}")

