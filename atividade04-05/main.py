from GrafoDenso import GrafoDenso

vertices = ['A', 'B', 'C', 'D', 'E']

e = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'D')]
g1 = GrafoDenso(vertices)

for u, v in e:
    g1.adicionar_aresta(u, v)

def usar_funções(f: GrafoDenso) -> None:
    print("Número de vértices:", f.numero_de_vertices())
    print("Número de arestas:", f.numero_de_arestas())
    print("Sequência de graus:", f.sequencia_de_graus())
    print("É simples? ", f.is_simples())
    print("É nulo? ", f.is_nulo())
    print("É completo? ", f.is_completo())
    f.imprimir()
    print()

g1.remover_aresta('A', 'C')

usar_funções(g1)

g2 = GrafoDenso(vertices)
usar_funções(g2)

g3 = GrafoDenso(vertices)
for i in vertices:
    for j in vertices:
        g3.adicionar_aresta(i, j)
usar_funções(g3)

g4 = GrafoDenso(vertices)
for i in vertices:
    for j in vertices:
        if i != j:
            g4.adicionar_aresta(i, j)
usar_funções(g4)