from GrafoDenso import GrafoDenso

v = ['A', 'B', 'C', 'D', 'E']
e = [('A', 'B'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('B', 'D')]
g = GrafoDenso(v)

for u, v in e:
    g.adicionar_aresta(u, v)

print("Número de vértices:", g.numero_de_vertices())
print("Número de arestas:", g.numero_de_arestas())
print("Sequência de graus:", g.sequencia_de_graus())
g.imprimir()
print()

g.remover_aresta('A', 'C')
print("Número de vértices:", g.numero_de_vertices())
print("Número de arestas:", g.numero_de_arestas())
print("Sequência de graus:", g.sequencia_de_graus())
g.imprimir()
